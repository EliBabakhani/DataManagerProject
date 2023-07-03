Here you go! 😎

# Let's Build a File Manager for a Game Development Company! 🎮

You are a junior Python developer working for a game development company. Your company has tasked you with building a file manager to manage the game assets 🎨, such as images, sounds 🔊, and other files needed for the game development process. The company wants a file manager that can store, retrieve, update, and delete files, as well as display a list of all the files stored in the manager. 

To make the project more interesting, your manager has given you a story to work with 📖:

"Your company is working on a new game called 'Lost in Space'. The game is set in a distant planet 🌌 where the player has to find their way back to Earth 🌍. The game has different levels, each with its own set of challenges. The company has hired a team of artists 🎨 and sound designers 🔊 to create the game assets, and it's your job to manage all these files in an organized way so that the development team can access them easily."

Your task is to create a file manager for the game assets. Let's get started! 🚀

## Step-by-Step Instructions: 📝

To complete this project, you need to follow these steps:

### Step 1: Understand the Codebase 🤔

The codebase for the file manager is already provided to you. The code is organized into three files:

- `base.py`: This file contains the base classes for the file manager, including `BaseModel` and `BaseManager`.
- `file_manager.py`: This file contains the implementation of the file manager class called `FileManager`. This class inherits from `BaseManager` and implements the methods for creating, reading, updating, and deleting files.
- `test.py`: This file contains the unit tests for the `FileManager` class. You can use these tests to ensure that your implementation is correct.

Read through the codebase and try to understand how the classes and methods are organized.

### Step 2: Implement the `read_all` Method 📋

The first step in building the file manager is to implement the `read_all` method in the `FileManager` class. This method should return a list of all the files stored in the manager. To implement this method, you need to:

- Use the `os` module to list all the files in the directory where the files are stored.
- Filter out any non-file objects, such as directories or links.
- Return a list of the remaining file objects.

Once you have implemented this method, run the `test3_read_all` test in `test.py` to ensure that it passes. 🙌

### Step 3: Implement the `create` Method 📝

The next step is to implement the `create` method in the `FileManager` class. This method should take a file object and create a new file in the manager. To implement this method, you need to:

- Generate a unique ID for the file object.
- Save the file object to a file with the unique ID as the file name.
- Return the unique ID.

Once you have implemented this method, run the `test1_create` test in `test.py` to ensure that it passes. 🙌

### Step 4: Implement the `read` Method 📖

The next step is to implement the `read` method in the `FileManager` class. This method should take a unique ID and return the file object with that ID. To implement this method, you need to:

- Load the file object from the file with the unique ID as the file name.
- Return the file object.

Once you have implemented this method, run the `test2_create_read` test in `test.py` to ensure that it passes. 🙌

### Step 5: Implement the `update` Method 🔄

The next step is to implement the `update` method in the `FileManager` class. This method should take a unique ID and a file object and update the file object with that ID. To implement this method, you need to:

- Load the file object from the file with the unique ID as the file name.
- Overwrite the contents of the file with the updated file object.

Once you have implemented this method, create a new test in `test.py` to ensure that it works correctly. 🙌

### Step 6: Implement the `delete` Method 🗑️

The final step is to implement the `delete` method in the `FileManager` class. This method should take a unique ID and delete the file object with that ID. To implement this method, you need to:

- Delete the file with the unique ID as the file name.

Once you have implemented this method, create a new test in `test.py` to ensure that it works correctly. 🙌### Step 7: Test Your Implementation 🧪

Once you have implemented all the methods, run the tests in `test.py` to ensure that your implementation works correctly. If all the tests pass, congratulations! 🎉 You have successfully built a file manager for your game development company! 🎮

### Bonus Step: Add Error Handling 🛡️

If you have extra time, you can add error handling to your file manager. For example, you can add checks to ensure that the file exists before trying to read or delete it, or add checks to ensure that the file is a valid file object before trying to create or update it. You can also add custom error messages to make it easier for developers to understand what went wrong.

To add error handling, you can use Python's built-in exception handling mechanisms, such as `try` and `except` blocks. You can raise custom exceptions when errors occur, and catch those exceptions in the higher-level code to provide more detailed error messages.

For example, you can add a custom `FileNotFoundError` exception to handle cases where a file with a given ID does not exist:

```python
class FileNotFoundError(Exception):
    pass

class FileManager(BaseManager):
    ...
 
    def read(self, id: int, model_cls: type) -> BaseModel:
        path = self._get_file_path(id, model_cls)
        try:
            with open(path, 'rb') as f:
                file_contents = pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File with ID {id} does not exist.")
        return file_contents
```

By adding error handling, you can make your file manager more robust and easier to use for developers. Good luck! 🍀
