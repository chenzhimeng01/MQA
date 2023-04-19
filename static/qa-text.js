const form = document.querySelector('form');
const answerDiv = document.querySelector('#answer');
const reasonDiv = document.querySelector('#reason');
const scoreDiv = document.querySelector('#score');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // 阻止表单默认行为

    // 将表单数据编码为 URL 编码格式的字符串
    const formData = new FormData(form)

    // 发送 POST 请求
    const response = await fetch('http://127.0.0.1:5000/qa-text', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    // 将响应内容呈现在页面上
    answerDiv.innerHTML = `Answer: ${result.answer}`;
    highlightText(result)
    scoreDiv.innerHTML = `Score: ${result.score}`;
});

function highlightText(result) {
    // 获取响应数据中需要高亮的部分的开始和结束位置
    const start = result.start;
    const end = result.end;

    // 将响应中的完整文本保存到一个变量中
    const text = result.context;

    // 将需要高亮的部分用 HTML 标签包裹起来，并添加 CSS 样式
    const highlightedText = '<span style="background-color: yellow;">' + text.slice(start, end) + '</span>';

    // 将高亮部分替换回原来的文本中
    const finalText = text.slice(0, start) + highlightedText + text.slice(end);

    // 将修改后的文本插入到页面中
    reasonDiv.innerHTML = `Reason: ${finalText}`;
}
