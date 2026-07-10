---
title: "ASCII-art-pt2"
datePublished: 2026-07-10T13:37:52.892Z
cuid: cmrezdfiw000009gi3rnw8u2j
slug: ascii-art-pt2

---

* * *

## ***What now?***

> As stated in the Future part in my Part1, my aim for Part 2 were to reduce redundancy in my code and create an input validation system that will print an error message until the user enters a valid input.

## ***2.1 Reduce redundancy***

*   To reduce redundancy, I decided to use two programming concepts. Functions and dictionaries.
    
*   As parts of my original code are highly repetitive (see [ascii1.py](http://ascii1.py)), hence by defining functions and passing in different arguments depending on the scenario, it allowed me to reuse the same code structure across categories. This reduced redundancy in my code and ensured that future changes only needed to be made at one place, improving maintainability.
    
*   As the ASCII arts take up a lot of space within the code, I have created dictionaries to store and organise them using its key-value pairs property and can be called later in my program. This allows the user inputs to correspond to the right art directly instead of a long and repeated if-elif statements and ASCII art.
    
*   As a result, I was able to eliminate approximately 38% of lines of code (from 417 to 259 lines). This has improved readability, simplified debugging, and made the program more scalable as now categories or ascii arts can be added or updated through dictionaries than duplicating sections of code (see [ascii1.py](http://ascii1.py)).
    

* * *

## ***2.2*** Example use of dictionary & functions

*   By uniting all the functions and dictionaries, I replaced the original manually written variables with automatic retrieval values stored in the dictionaries. This let the program to show the correct category and ASCII art based on the user’s input (keys) while reducing code repetition (Image1).
    
*   For example, the variable `ans` captures the input of the user's chosen category. This variable then becomes the argument for the function `section` and the key value for `dict_start`.
    
*   The dictionary stores the relationship between the user’s input (a, b, c, or d) and the corresponds category name and ascii art. I then insert this dictionary into my function, so it is reusable.
    

<details data-node-type="hn-details-summary">
<summary>Image 1 + Image 2</summary>
<img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/d21286f6-7765-4366-bb54-e269327eabc6.png" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/7dbfabcb-2fdb-4269-aed4-1fa2f4d6d98a.png" isuploading="false" align="center">
</details>

*   Dictionary for the name of each category in ascii and ascii for animal section
    

<details data-node-type="hn-details-summary">
<summary>Image 3 + 4</summary>
<img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/1435d412-c24e-4761-a827-965d8f6ede10.png" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/a74aa44e-9e35-4f5b-a422-b4c486039bda.png" isuploading="false" align="center">
</details>

*   I also imported the random library so I can randomise the “Choose random” option section. As this is also a highly repetitive part in my original code, by defining once with a function, this made the code shorter, cleaner, and maintainable.
    

<details data-node-type="hn-details-summary">
<summary>Image 5</summary>
<img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/bcea6084-1e18-495b-87a2-371e911ad0d2.png" isuploading="false" align="center">
</details>

* * *

## ***2.3 Create Error message***

*   As the code from Part1 only returns ‘error’ and stops running when it doesn’t match any conditions, it’s not very user friendly. Hence, I have created a validation loop using a while statement. This improves the user experience by preventing the program from terminating when invalid input (such as a typo) was entered and only valid options are processed and eventually lead to an ASCII art.
    

<details data-node-type="hn-details-summary">
<summary>Image 6</summary>
<img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/26cf3efe-4b43-4e82-92cd-4089455703ba.png" isuploading="false" align="center">
</details>

* * *

## ***2.4 Summary***

*   Difficulties: Surprisingly the difficult part this time wasn’t about the code itself, it was about breaking down the problem and what I can use to achieve the features I want while ensuring that the program is still readable, maintainable, and working. It required very careful planning and restructuring the code as one wrong variable can break the whole program.
    
*   Future: enable users to import their own ascii art into my program which will make it more interactive.  Additional ascii categories and maybe even a graphical user interface (GUI) could also be added.
    
*   Evaluation: Overall, the goals for Pt2 of this project were successfully met. The program has not only become more efficient through functions and dictionaries, but it also reduced redundancy and improved maintainability. The input validation also prevents users from causing errors and can keep inputting until they reach a cute ascii art. Hecne, these improvements make the application more scalable for future expansions.