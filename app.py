import streamlit as st

def task_management_app():
    st.title("Task Management App")
    st.write("Welcome to the Task Management App! Use this tool to manage your daily tasks.")

    # Initialize session state for tasks if not already done
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    # Add tasks
    with st.form(key="task_form"):
        total_task = st.number_input("How many tasks do you want to add?", min_value=1, step=1)
        task_inputs = []
        for i in range(total_task):
            task_name = st.text_input(f"Enter task {i + 1}", key=f"task_{i}")
            task_inputs.append(task_name)

        submit = st.form_submit_button("Add Tasks")
        if submit:
            st.session_state.tasks.extend(task_inputs)

    # Display tasks
    st.write("### Today's Tasks")
    if st.session_state.tasks:
        for i, task in enumerate(st.session_state.tasks, 1):
            st.write(f"{i}. {task}")
    else:
        st.write("No tasks added yet.")

    # Update tasks
    st.write("### Update Tasks")
    task_to_update = st.number_input("Enter the task number to update", min_value=1, step=1, max_value=len(st.session_state.tasks) if st.session_state.tasks else 1)
    new_task_name = st.text_input("Enter the new task name")
    if st.button("Update Task"):
        if st.session_state.tasks and 1 <= task_to_update <= len(st.session_state.tasks):
            st.session_state.tasks[task_to_update - 1] = new_task_name
            st.success("Task updated successfully!")
        else:
            st.error("Invalid task number.")

    # Clear all tasks
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.success("All tasks cleared!")

if __name__ == "__main__":
    task_management_app()
