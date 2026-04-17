import streamlit as st
import requests
import time

st.set_page_config(page_title="UCAS LLP - 小模型实验平台", page_icon="🧪", layout="centered")

st.title("🧪 UCAS 小模型实验平台")
st.caption("实验性 Demo — 基于 Ollama / gemma4")

backend_URL = "http://192.168.43.10:8080/api/qwen"
DEFAULT_MODEL = "gemma4:e4b"

# ── 侧边栏：参数调节 ──
st.sidebar.header("⚙ 生成参数")
temperature = st.sidebar.slider("temperature", 0.0, 2.0, 0.7, 0.1)
top_p = st.sidebar.slider("top_p", 0.0, 1.0, 0.9, 0.05)
max_tokens = st.sidebar.slider("max tokens", 50, 2000, 800, 50)
model = st.sidebar.text_input("model", DEFAULT_MODEL)

# ── 快捷提示词 ──
st.sidebar.markdown("---")
st.sidebar.markdown("**💡 快捷提示**")
quick_prompts = {
    "写一首诗": "写一首关于春天的短诗，四句即可。",
    "讲个笑话": "讲一个简短的笑话。",
    "解释概念": "用一句话解释什么是机器学习。",
    "续写故事": "从前有座山，山上有座庙，",
}
for label, prompt_text in quick_prompts.items():
    if st.sidebar.button(label):
        st.session_state["prompt"] = prompt_text

# ── 主输入区 ──
st.markdown("### 输入提示词")
if "prompt" not in st.session_state:
    st.session_state["prompt"] = ""
user_input = st.text_area(
    "输入你的提示词：",
    value=st.session_state["prompt"],
    height=120,
    key="input_area",
)

col1, col2, col3 = st.columns([1, 1, 4])
run_btn = col1.button("🚀 生成", type="primary")
clear_btn = col2.button("🗑 清空")

if clear_btn:
    st.session_state["response"] = ""
    st.rerun()

# ── 生成逻辑 ──
if run_btn and user_input.strip():
    with st.spinner("模型生成中..."):
        payload = {
                      "model": model,
                      "messages": [
                        {
                          "role": "user",
                          "content": user_input
                        }
                      ],
                      "stream": False
                    }
        try:
            start = time.time()
            res = requests.post(backend_URL, json=payload)
            elapsed = round(time.time() - start, 2)
            res.raise_for_status()
            response_text = res.json()
            st.session_state["response"] = response_text.get("content"," none ")
            st.session_state["elapsed"] = elapsed
            st.session_state["error"] = ""
        except requests.exceptions.ConnectionError:
            st.session_state["error"] = (
                f"❌ 无法连接 Ollama ({backend_URL})\n"
                f"请确认 Ollama 已启动：`ollama serve`\n"
                f"并拉取模型：`ollama pull {model}`"
            )
            st.session_state["response"] = ""
        except requests.exceptions.Timeout:
            st.session_state["error"] = "⏱ 请求超时，模型响应时间过长"
            st.session_state["response"] = ""
        except Exception as e:
            st.session_state["error"] = f"❌ 错误: {e}"
            st.session_state["response"] = ""
    st.rerun()

# ── 展示结果 ──
st.markdown("---")
st.markdown("### 生成结果")

if st.session_state.get("error"):
    st.error(st.session_state["error"])
elif st.session_state.get("response"):
    st.markdown(st.session_state["response"])
    st.caption(
        f"耗时: {st.session_state.get('elapsed', '?')}s  |  "
        f"tokens: {max_tokens}  |  "
        f"temperature: {temperature}"
    )
    # ── 复制按钮 ──
    st.download_button(
        label="📋 下载结果 (txt)",
        data=st.session_state["response"],
        file_name="response.txt",
        mime="text/plain",
    )
else:
    st.info("在上方输入提示词，点击「生成」开始实验。")
