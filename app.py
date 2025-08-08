from flask import Flask, render_template, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, MessageGraph


app = Flask(__name__)


# Set up a simple LangGraph workflow using Gemini via LangChain
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
graph_workflow = MessageGraph()
graph_workflow.add_node("agent", model)
graph_workflow.add_edge("agent", END)
graph_workflow.add_edge(START, "agent")
agent = graph_workflow.compile()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json() or {}
    system_prompt = data.get('system_prompt', '')
    user_prompt = data.get('user_prompt', '')
    text_blocks = data.get('text_blocks', '')

    messages = [
        ("system", system_prompt),
        ("user", text_blocks),
        ("user", user_prompt),
    ]

    try:
        result = agent.invoke(messages)
        response_text = result[-1].content
    except Exception as e:
        response_text = f"Error: {e}"

    return jsonify({'output': response_text})


if __name__ == '__main__':
    app.run(debug=True)
