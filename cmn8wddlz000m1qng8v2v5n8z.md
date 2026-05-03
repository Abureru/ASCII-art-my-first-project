---
title: "ASCII-ART Pt 1 "
datePublished: 2026-03-27T12:48:25.131Z
cuid: cmn8wddlz000m1qng8v2v5n8z
slug: ascii-art-pt-1

---

**As this is my very first project (and I hope this is the first one people will check T^T) I will do a little short intro:**

> Hi, my name is Abureru (Avril), and I am documenting my journey studying advanced computer science majoring in AI. Here I will organise and document my projects whether it's for myself or for uni (please ignore my grammatical errors). I am hoping to make some cool, cute, fun, and useful projects to help me in my everyday life, if not make it <s>lazier</s> more fulfilling (and hopefully get a j\*b out of it :D).

## *About the project*

*   <mark class="bg-yellow-200 dark:bg-yellow-500/30">What:</mark> This is an ASCII art project where when a user inputs the guided answer from the Python program, it will output either (a) more options, which will then eventually lead to (b) the actual ASCII art. To do this, I have included four different sections for the user to choose from: (1) Animals, (2) Music instruments, (3) Plants, (4) Buildings. In each section I have included one big ASCII art title with three ASCII art to choose from. Hence after the user inputs a wanted section, they can then choose whether they would like to have their ASCII art to be outputted as (a) random or (b) given the three selections which they then pick.
    
*   <mark class="bg-yellow-200 dark:bg-yellow-500/30">Why:</mark> This is a project for me. As I just began *Python,* I believe the best way to learn is to actually make something. And I like ASCII art because they are cute and expressive :33!
    
*   <mark class="bg-yellow-200 dark:bg-yellow-500/30">How:</mark> This is built using the popular programming language *Python* through an IDE called *Thonny* (what we use in Uni). The art source was extracted from an [ASCII art archive](https://www.asciiart.eu/gallery).
    

* * *

## *How it works*

\- By using a built-in function `print ()` and writing text inside quotes `' '`, Python then treats it as plain text and displays it exactly as it is.

\- By using another built-in function `input ()`, I can invite the user to interact with the program. I then assign this response to the variable `ans` which then allows me to manipulate that input for later uses.

<details data-node-type="hn-details-summary">
<summary>Code Part 1 (What I wrote)</summary>
<img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/8d0af11d-52c3-4a89-8db6-0be5a94185a6.png" isuploading="false" align="center">
</details><details data-node-type="hn-details-summary">
<summary>Output Part 1 (What the user will see)</summary>
<img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/2e7ced83-c563-417d-8065-6a1a4fd75cab.png" alt="Shell 1" isuploading="false" align="center">
</details>

\- By using the `if-elif-else` statement, I enabled my program to output different Ascii art tiles depending on the situation.

\- There were three things that caught me off guard in this section: (1) `==`, (2)`:`, (3) `""" """`.

(1) At first, I used `=` thinking that when `ans` equals to `a` it will print, however in *Python*, `=` is the **assignment operator** used to store a value in a variable, while `==` is the **comparison operator** used to check whether two values equate.

(2) This was just me forgetting the syntax T^T

(3) This issue was accounted during inserting the ASCII art. At first, I only used `' '` but because the art itself contains many symbols which caused a syntax error. This is resolved by using triple quotes `""" """` to tell *Python* to treat everything inside as a plain text so it stops trying to interpret the symbols as code.

<details data-node-type="hn-details-summary">
<summary>Code Part 2 (What I wrote)</summary>
<img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/002653f9-8057-45c6-b291-06888af40ec0.png" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/fcfda396-79f0-46d8-a948-c171e2606b42.png" alt="" title="" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/bc62cf1c-3dbd-4822-82d0-7d56c63ad515.png" alt="" title="" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/5de51fba-36dc-47c9-8dd9-367d7008bf84.png" alt="" title="" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/e0a9fb30-651d-4c57-8030-c61ef160a74d.png" alt="" title="" isuploading="false" align="left">
</details><details data-node-type="hn-details-summary">
<summary>Output Part 2 (What the user will see)</summary>
<p>Here is what the user will see when they input different answers.</p><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/ee1ea658-0916-4995-9e8d-e5f0467bdcc9.png" alt="" title="" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/35b7650c-0c35-4f88-a62f-bd1ec865fde6.png" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/56eec667-f19f-4dd9-84e3-30a22e001ca0.png" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/aa94db8a-e184-4262-a63e-e7698ffad061.png" alt="" title="" isuploading="false" align="center"><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/e7b10cbf-46b7-44e7-82ca-fd6edf1e7815.png" isuploading="false" align="center">
</details>

\- To make the program more interactive, I have decided to give the user two options (1) To output the Ascii- art randomly or (2) Let the user to see their options first then decide which art to output.

\- This is done again by assigning the `input` into a variable `choice1`. As I had no idea how to make *Python* to randomly generate one of my responses, I had the help of *Google* and found out that random is a *Python import statement* and needs to be imported into the code. I then put that with an `if-elif-else` statement as the other condition will be used for outputting (1) see my option (2) error.

\- Since I only have three Ascii arts to output for every section, I use the random function to generate a random number between 1 to 3 inclusive. Then I assign each number with a specific art. Another `if-elif` statement was used to give me three conditions: output 1 for a cat, 2 for a dog, and 3 for a wolf.

\- Moving on to option (b), for this one I just printed out the three available options and used another `if-elif-else` statement to allow different responses (in letters), and I assign each option to a specific Ascii-art.

\- Lastly, if the input doesn't match any condition, the program returns an error.

<details data-node-type="hn-details-summary">
<summary>Code Part 3 (What I wrote)</summary>
<img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/2d43b846-6886-4811-a6f3-ccc34c148bc3.png" isuploading="false" align="center">
</details><details data-node-type="hn-details-summary">
<summary>Output Part 3 (What the user will see) Reminder:</summary>
<p>Reminder: This is only one art section out of the four possible sections as there is simply not enough space T^T. But the other three sections do have the same layout.</p><p></p><p>Here is (1):</p><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/45bb7589-01f8-4264-a0a2-608a2dca1d20.png" isuploading="false" align="center"><p>Here is (2):</p><img class="rounded-lg max-w-full h-auto" src="https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/01863ff8-f341-4ada-899a-851683b4ae3f.png" isuploading="false" align="center">
</details>

Source code in GitHub.

* * *

*   <mark class="bg-yellow-200 dark:bg-yellow-500/30">Difficulties:</mark> It was quite challenging as this is the first coding in my life. There were also issues raised about syntax errors, operators, and import statement throughout the ***How it works*** section. Lastly, as there were many repeated code in and out and with ASCII art taking lots of space, it was hard to navigate through the code, which proved to be highly problematic when you come back to it the next day or trying to debug the code.
    
*   <mark class="bg-yellow-200 dark:bg-yellow-500/30">Future:</mark> As the program only returns 'error' and stops running if the input doesn't match any condition, hence the program might be more functional if it loops back to the input prompt until the user enters something that matches. Furthermore, to resolve the last problem from difficulties, the aim is to introduce functions which will reduce code repetition and make the code easier to navigate.