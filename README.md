<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
</head>
<body>

<p><strong>LibraryPy</strong></p>

<p>
Author: Coen Howerter<br>
Version: 1.0.0<br>
Date: December 10, 2025
</p>

<p>
LibraryPy is a database driven application designed to store and organize Python libraries and their associated
functions in a centralized reference system. The application provides a graphical user interface for browsing
libraries by topic and can be distributed as a standalone executable that does not require a Python installation
for end users.
</p>

<p>
The purpose of this project is to provide a structured and searchable reference tool for exploring Python libraries,
their functionality, and example usage.
</p>

<p><strong>Application Description</strong></p>

<p>
The graphical interface is organized into three columns:
</p>

<ul>
    <li>
        The left column displays topic based tags used to categorize libraries. Each library may be associated
        with multiple tags.
    </li>
    <li>
        The middle column displays libraries associated with the selected tag.
    </li>
    <li>
        The right column displays the functions associated with the selected library.
    </li>
</ul>

<p>
For each function, the following information is shown:
</p>

<ul>
    <li>Function name</li>
    <li>Description of the function</li>
    <li>Example usage</li>
</ul>

<p>
This layout allows for efficient browsing and contextual understanding of library functionality.
</p>

<p><strong>Repository Structure</strong></p>

<pre>
LibraryPy/
├── Additions/
│   ├── add_to.py
│   └── library_explorer.py
├── DataBase_Specs/
│   ├── Library_items.db
│   ├── icon.ico
│   └── library_explorer.spec
├── test/
│   ├── Items_Query
│   ├── Library_Query
│   └── Tags_Query
├── library_explorer.exe
└── README.md
</pre>

<p>
The Additions directory contains scripts used to modify the database and build the application.
The DataBase_Specs directory contains the SQLite database, build specification files, and application resources.
The test directory contains scripts used to query and validate database contents.
</p>

<p><strong>Running the Application</strong></p>

<p>
End users may run the compiled executable directly:
</p>

<pre>
library_explorer.exe
</pre>

<p>
No additional dependencies or installations are required.
</p>

<p><strong>Adding Libraries and Functions</strong></p>

<p>
Libraries, tags, and functions can be added to the database using the script
<code>add_to.py</code> located in the Additions directory.
</p>

<ol>
    <li>Edit <code>Additions/add_to.py</code> to include new libraries, tags, or items.</li>
    <li>Run the script using Python:</li>
</ol>

<pre>
python add_to.py
</pre>

<p>
This updates the SQLite database file located at
<code>DataBase_Specs/Library_items.db</code>.
</p>

<p><strong>Rebuilding the Executable</strong></p>

<p>
After modifying the database, the executable must be rebuilt so that the updated data is included.
</p>

<p>
To generate a standalone executable from <code>library_explorer.py</code>, ensure that the following files are
present in the same directory:
</p>

<ul>
    <li><code>library_explorer.py</code></li>
    <li><code>Library_items.db</code></li>
    <li><code>icon.ico</code> (optional, used as the application icon)</li>
</ul>

<p>
Build the executable using PyInstaller:
</p>

<pre>
pyinstaller --onefile --windowed --icon=icon.ico library_explorer.py
</pre>

<p>
After the build completes, the executable will be created in the <code>dist</code> directory as
<code>library_explorer.exe</code>. This executable can be run independently and does not require a Python installation
on the target system.
</p>

<p><strong>Testing and Validation</strong></p>

<p>
The test directory contains scripts used to query the database directly from the terminal. These scripts are
intended for validation and debugging and allow verification of tags, libraries, and items without using the
graphical interface.
</p>

</body>
</html>
