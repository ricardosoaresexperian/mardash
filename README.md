# mardash
Marimo Dashboard

based on https://bury-thomas.medium.com/deploy-a-python-dashboard-to-github-pages-with-marimo-no-backend-all-free-7bda3acee3ef

lets try
```python
eh = pyo.code.run_js("""
const url = 'https://jsonplaceholder.typicode.com/posts/1';
  
fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json(); // Converts response stream to a JS object
  });
""")
````

ver wasmtime

https://jsonplaceholder.typicode.com/posts/1