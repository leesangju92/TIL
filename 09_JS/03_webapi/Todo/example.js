const init = () => {
    const todoBox = document.querySelector('#todo_box');
    const reverseButton = document.querySelector("#reverse_btn");
    const fetchButton = document.querySelector("#fetch_btn");

    const createTodo = (inputText, completed=false) => {
        const todoCard = document.createElement('div');
        todoCard.classList.add('ui', 'segment', 'todo-item');

        const wrapper = document.createElement('div');
        wrapper.classList.add('ui', 'checkbox');

        const input = document.createElement('input');
        input.setAttribute('type', 'checkbox');
        // input.checked = completed;
        input.addEventListener('click', e => {
            if (input.checked) {
                label.classList.add('completed-label');
                todoCard.classList.add('secondary');
                // completed = true;
            } else {
                label.classList.remove('completed-label');
                todoCard.classList.remove('secondary');
                // completed = false;
            }
        });

        const label = document.createElement('label');
        label.innerText = inputText;
        if (completed) label.classList.add('completed-label');

        const deleteIcon = document.createElement('i');
        deleteIcon.classList.add('close', 'icon', 'delete-icon');
        deleteIcon.addEventListener('click', e => {
            todoBox.removeChild(todoCard);
        });

        wrapper.appendChild(input);
        wrapper.appendChild(label);
        todoCard.appendChild(wrapper);
        todoCard.appendChild(deleteIcon);

    };
// todoBox.appendChild(createTodo('Hi'));
// todoBox.appendChild(createTodo('Bye', false));

// TODO: input, Add 버튼에 createTodo와 이벤트 리스너를 잘 버무린다.

    const reverseTodos = () => {
        const allTodos = Array.from(document.querySelectorAll(".todo-item"));
        while (todoBox.firstChild) {
            todoBox.removeChild(todoBox.firstChild)
        }
        for (const todo of allTodos.reverse()) {
            todoBox.appendChild(todo)
        }
    };

// TODO: 버튼 만들고, 데이터 받아오게 이벤트 리스너를 클릭과 연관지어서..

    const fetchData = URL => {
        fetch(URL)
            .then(res => res.json())
            .then(todos => {
                for (const todo of todos) {
                    createTodo(todo.title)
                }
            })
    };

    const pushToDom = (where, what) => {
        where.appendChild(what);
    };

    reverseButton.addEventListener("click", e=> {
        reverseTodos()
    });

    fetchData("https://koreanjson.com/todos");
};

init();