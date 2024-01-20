// Inside the TaskForm component

// Add state to track form input and error
const [task, setTask] = useState("");
const [error, setError] = useState("");

// Handle form submission
const handleSubmit = (e) => {
  e.preventDefault();

  if (task.trim() === "") {
    setError("Task field cannot be empty");
    return;
  }

  // Proceed with submitting the task
  // Your code to create/update the task goes here

  // Reset form input and error state
  setTask("");
  setError("");
};

// Render the task form
return (
  <form onSubmit={handleSubmit}>
    {/* Task input field */}
    <input
      type="text"
      value={task}
      onChange={(e) => setTask(e.target.value)}
    />

    {/* Error message */}
    {error && <p>{error}</p>}

    {/* Submit button */}
    <button type="submit">Add Task</button>
  </form>
);
