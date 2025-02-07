# tests/test_project.py
import subprocess
import pytest

@pytest.fixture(scope="module")
def compile_project():
    """Fixture to compile the C++ project."""
    result = subprocess.run(["make"], capture_output=True, text=True)
    if result.returncode != 0:
        pytest.fail(f"Compilation failed:\n{result.stderr}")
    return "bin/university_system"

def test_program_output(compile_project):
    """Test the output of the compiled program."""
    # Run the compiled executable
    executable = compile_project
    result = subprocess.run([executable], capture_output=True, text=True)

    # Check if the program ran successfully
    assert result.returncode == 0, f"Program execution failed:\n{result.stderr}"

    # Expected output (customize based on your implementation)
    expected_output = """
Student: John Doe
Age: 20
Enrolled Courses:
- Math 101
- Physics 101

Professor: Dr. Smith
Age: 45
Assigned Courses:
- Math 101
- Chemistry 101

Department: Science Department
Professors:
- Dr. Smith
  Assigned Courses:
  - Math 101
  - Chemistry 101
Courses:
- Math 101
  Enrolled Students:
  - John Doe
- Physics 101
  Enrolled Students:
  - Jane Doe
"""

    # Validate the output
    assert result.stdout.strip() == expected_output.strip(), (
        f"Output mismatch:\nExpected:\n{expected_output}\nGot:\n{result.stdout}"
    )

def test_clean_up():
    """Test cleanup by running 'make clean'."""
    result = subprocess.run(["make", "clean"], capture_output=True, text=True)
    assert result.returncode == 0, f"Cleanup failed:\n{result.stderr}"
