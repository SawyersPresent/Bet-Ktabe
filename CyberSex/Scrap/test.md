
## 1. Basic Structure of a C++ Program

Every C++ program begins with the special function `main()`, which is the **entry point**. Before it, we use `#include` directives to import standard libraries.

The program executes instructions sequentially and typically ends with `return 0`, signaling successful execution.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-2-input-and-output-io)2. Input and Output (I/O)

In C++, input is handled through the **standard input stream** (usually the keyboard), and output is printed to the **console**.

We use tools from the standard library for this, like `cin` for input and `cout` for output, both of which are part of the `std` (standard) namespace.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-3-variables-and-data-types)3. Variables and Data Types

C++ is **strongly typed**, meaning every variable must be declared with a type: `int`, `float`, `char`, `bool`, etc.

Memory for these variables is stored either on the **stack** (for local/static allocation) or on the **heap** (for dynamic allocation).

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-4-control-flow)4. Control Flow

Control flow structures allow decision-making and repetition:

- **Conditionals:** `if`, `else if`, `else` evaluate boolean conditions.
- **Loops:** `for`, `while`, `do-while` repeat actions until a condition fails.
- **Switch-case:** handles multiple cases for a single variable.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-5-functions)5. Functions

Functions group reusable logic. They can accept parameters and return values. Functions make code modular and reusable.

C++ supports **function overloading**, allowing multiple functions with the same name but different parameter types.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-6-pointers-and-references)6. Pointers and References

- **Pointers** hold memory addresses and are key in low-level programming.
- **References** are aliases for existing variables and allow functions to modify original values **without copying**.

Both are essential for performance and interoperability with system-level APIs.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-7-dynamic-memory-allocation)7. Dynamic Memory Allocation

C++ allows memory allocation during program execution using the `new` and `delete` operators.

This memory lives on the **heap**, and it's your responsibility to release it using `delete` to prevent **memory leaks**.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-8-arrays-and-c-style-strings)8. Arrays and C-style Strings

- **Arrays** are fixed-size sequences of elements.
- **C-style strings** are arrays of `char` terminated by a null character (`'\0'`).

String operations must be done safely using functions like `strcpy_s` instead of `strcpy` to avoid buffer overflows.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-9-structs-enums-and-type-aliases)9. Structs, Enums, and Type Aliases

- **Structs:** Group related variables into one logical unit.
- **Enums:** Define sets of named integer constants for readability.
- **Typedef / using:** Create aliases for types to simplify complex type declarations.

These are frequently used in Windows API data structures and system-level programming.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-10-object-oriented-programming-oop)10. Object-Oriented Programming (OOP)

C++ supports full OOP principles:

- **Classes:** Define data (attributes) and behavior (methods).
- **Encapsulation:** Control access using `public`, `private`, `protected`.
- **Constructors/Destructors:** Special methods to initialize and clean up objects.
- **Inheritance/Polymorphism:** Reuse and extend code, allow dynamic behavior.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-11-namespaces-and-std)11. Namespaces and `std::`

Namespaces group related symbols and prevent name collisions.

The `std::` namespace contains all standard library features. You can either:

- Use `std::cout` explicitly, or
- Write `using namespace std;` (discouraged in large or critical projects)

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-12-smart-pointers)12. Smart Pointers

C++ offers smart pointers for **automatic memory management**:

- **`unique_ptr`:** Exclusive ownership; memory is freed when the pointer is destroyed.
- **`shared_ptr`:** Reference-counted; memory is freed when the last reference is gone.

Smart pointers help prevent **memory leaks** and **dangling pointers**.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-13-templates)13. Templates

Templates enable **generic programming**, allowing the same function or class to work with any data type.

They are foundational to the Standard Template Library (STL) and support code reuse and type safety.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-14-lambda-expressions)14. Lambda Expressions

Lambdas are **anonymous functions** defined inline. They're used for short, reusable logic, especially in:

- Sorting
- Filtering
- Callbacks
- Threading

They can capture variables from their surrounding scope by value or reference.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-15-move-semantics-stdmove)15. Move Semantics (`std::move`)

Move semantics let you **transfer resources** from one object to another without copying.

Using `std::move`, you can avoid expensive operations when dealing with large data like strings or buffers.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-16-exception-handling)16. Exception Handling

C++ uses exceptions to handle runtime errors gracefully:

- `try`: Marks a block that might fail.
- `throw`: Triggers an error.
- `catch`: Handles specific exceptions.

This helps prevent crashes and allows for **robust error recovery**.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-17-raii-resource-acquisition-is-initialization)17. RAII (Resource Acquisition Is Initialization)

A C++ idiom where resources like memory, file handles, or locks are **tied to object lifetimes**.

When the object goes out of scope, its destructor is called automatically, releasing the resource.

This pattern is followed by:

- File streams
- Smart pointers
- Lock guards (thread synchronization)

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-18-standard-template-library-stl)18. Standard Template Library (STL)

The STL provides a powerful set of containers and algorithms:

- **Containers:** `vector`, `map`, `set`, `queue`, etc.
- **Algorithms:** `sort`, `find`, `for_each`, etc.
- **Iterators:** Abstract pointers to traverse containers.

STL code is highly reusable, efficient, and tested.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-19-preparation-for-windows-api-development)19. Preparation for Windows API Development

To interact with the Windows operating system, C++ is the best-suited language due to:

- Direct memory access
- Struct manipulation
- Pointer-level control
- Full compatibility with C (the language of WinAPI)

Common tasks include:

- Including `<Windows.h>`
- Using wide strings (`wchar_t`, `L"string"`)
- Managing `HANDLE` types and `DWORD`, `LPVOID`, etc.
- Calling native functions like `CreateProcessW`, `VirtualAlloc`, `MessageBoxW`

Knowledge of **structures, pointers, and memory models** is essential for working with the Windows kernel, system calls, and EDR evasion.

---

## [](https://redteamleaders.coursestack.com/courses/96e8cffc-ac6e-4605-b7e1-39c6c26bd2e8/take/c-concepts#user-content-summary-of-topics)Summary of Topics

| Category            | Concepts Covered                                               |
| ------------------- | -------------------------------------------------------------- |
| Fundamentals        | Program structure, variables, I/O                              |
| Control Structures  | if, for, while, switch                                         |
| Functions           | Declaration, parameters, overloading                           |
| Memory & Pointers   | Pointers, dynamic allocation, nullptr                          |
| Data Aggregation    | Arrays, structs, enums, type aliases                           |
| OOP                 | Classes, constructors, methods, encapsulation                  |
| Advanced Concepts   | Smart pointers, templates, lambdas, exceptions, move semantics |
| RAII & Safety       | Scope-based resource management                                |
| STL                 | Vectors, iterators, algorithms                                 |
| Windows Integration | Windows.h, handles, wide strings, API structs                  |