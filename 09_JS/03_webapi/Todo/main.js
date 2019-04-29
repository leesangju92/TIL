const init = () => {
    const todoBox = document.querySelector('#todo_box');
    const reverseButton = document.querySelector("#reverse_btn");
    const fetchButton = document.querySelector("#fetch_btn");
    const addTodoButton = document.querySelector("#add_todo_btn");
    const addTodoInput = document.querySelector("#add_todo_input");

    addTodoButton.addEventListener("click", e => {
        createTdo(addTodoInput.value);
    });

    addTodoInput.addEventListener("keydown", e => {
        if (e.code === "Enter") {
            createTdo(addTodoInput.value);
        }
    });

    reverseButton.addEventListener("click", e => {
       reverseTodos();
    });

    fetchButton.addEventListener("click", e => {
        fetchTodos("https://koreanjson.com/todos")
    });

    const createTdo = (inputText, completed=false) => {
        const todoCard = document.createElement('div');
        todoCard.classList.add('ui', 'segment', 'todo-item');


        const wrapper = document.createElement('div');
        wrapper.classList.add('ui', 'checkbox');


        const input = document.createElement('input');
        input.setAttribute('type', 'checkbox');

        input.checked = completed;

        input.addEventListener("click", e => {
            if (input.checked) {
                label.classList.add("completed-label");
                todoCard.classList.add("secondary");
            } else {
                label.classList.remove("completed-label");
                todoCard.classList.remove("secondary");
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
        todoBox.appendChild(todoCard);

    };

    const reverseTodos = () => {
      const allTodos = Array.from(document.querySelectorAll(".todo-item"));
      while (todoBox.firstChild) {
          todoBox.removeChild(todoBox.firstChild)
      }
      for (const todo of allTodos.reverse()) {
          todoBox.appendChild(todo)
      }
    };

    const fetchTodos = URL => {
        fetch(URL).then(res=>res.json()).then(todos => {
            for (const todo of todos) {
                createTdo(todo.title, todo.completed) }
        })
    }
};

init();