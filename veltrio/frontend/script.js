async function sendInput() {
  const input = document.getElementById('textInput').value;
  const res = await fetch('http://localhost:8000/process/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: input })
  });
  const data = await res.json();
  document.getElementById('output').innerText = `Translation: ${data.translated}\nSentiment: ${data.sentiment}`;
}