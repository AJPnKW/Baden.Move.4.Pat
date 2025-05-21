function renderTodo(containerId) {
  const container = document.getElementById(containerId);
  const list = document.createElement('ul');
  list.style.listStyle = 'none';
  const tasks = [{ text: 'Sample Task 1', status: 'todo' }, { text: 'Task 2', status: 'in-progress' }, { text: 'Done task', status: 'done' }];
  tasks.forEach(item => {
    const li = document.createElement('li');
    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.checked = item.status === 'done';
    cb.onchange = () => item.status = cb.checked ? 'done' : 'todo';
    li.appendChild(cb);
    li.appendChild(document.createTextNode(' ' + item.text));
    list.appendChild(li);
  });
  container.appendChild(list);
}