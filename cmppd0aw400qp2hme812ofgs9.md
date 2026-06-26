---
title: "Pt.2. Intro to Desmos (Basic graphing)"
datePublished: 2026-05-28T10:37:52.038Z
cuid: cmppd0aw400qp2hme812ofgs9
slug: pt-2-intro-to-desmos-basic-graphing

---

> Disclaimer: this is just a side hobby and is not heavily related to cs topics. The following guide is based on my experience with Desmos and may contain inaccuracies or shortcomings. I am sorry for any grammatical errors. I am also working on a video version on YT.

Before we move on to the practical par, I strongly recommend checking out my Pt1 beforehand, where I have covered the Desmos interface. Now without further a due, let's start!

* * *

### 1\. Variables + Sliders

![](https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/82a53a7d-71bd-4fff-ab15-da92d26a23cd.png align="center")

Variables in mathematics are letters that can be replaced by numbers, which can be used to manipulate graphs. One of the cool things that Desmos allows us to do is a slider. As I can't physically show you its capability, just input a slider and it will ask you to add slider and once you click on that u can slide around by holding down the dot.

You can also increase the range by clicking and changing the end points, and if you would like a specific value you can click on the expression and change the number manually. It helped me a lot when I first started Desmos as I wasn't very sure on how wildly a value can change the graph, and with the help of the slider, not only do you get a feel of that, you can also see how it transitions based on the change in number.

It is also very useful if you ever want to go down Desmos animation or anything that involves a continue change in graph and/or variable.

* * *

## 2\. Restrictions (domain & range)

![](https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/3c883739-286f-4c20-bd01-da73bc3c3803.png align="center")

Domain and range restrict where the graph appears, which is VERY important for tracing and controlling graphs.

If you think about it, x, without any restriction, can be any value ranging from -♾️ to +♾️, that is why y maps to any possible solutions that is thrown by x. Since it would be unpleasant to use an endless line for drawing, that's when we need domain (restrict x-value) and range (restrict y-value).

Example:

```plaintext
y=x {0 ≤ x}
```

The equation is y = x. This linear would have had mapped itself from -♾️ to +♾️, however, because I have put a domain restriction on the graph (in the curly brackets). This basically tells Desmos, "For this equation, only show me the graph where x is bigger than or equals to 0!" You can also use < instead of ≤ as visually it is too small to see the difference anyway.

* * *

### 3\. Equations & Relations:

Here are some common equations and relations that I often use to draw in Desmos:

$$y = a(x-b)^2 + c$$

$$(x-a)^2 + (y-b)^2 = c$$

$$x = a(y-b)^2 + c$$

$$(x-y-a)^2 + (y-b)^2 = c$$

$$y= asin(bx-c)+d$$

$$x = asin(by-c)+d$$

I often only use ellipses, parabolas, sin, and linear. Any variables other than x or y modifies the graphs by either translating them or dilating them. My strongest recommendation is to plug in these graphs and change the value of each variable by adding in sliders to see how the graphs changes.

* * *

## 4\. Smooth joints (Visually smooth VS mathematically smooth)

Since we been through the graphs in section 3 and how to restrict it by using domain and/or range in section 2, let's move on to my only technique :D

If you have seen my artwork from [YouTube](https://www.youtube.com/@yoru_akuji/shorts), you can see that my first couple of shorts are not as appealing as the lines do not connect properly. However, as I further explore and studied calculus, I have implemented some of that knowledge into Desmos, and I named it **visually smooth joints** (there might be a proper math term for that that someone already came up with before me and if that's so I apologise) I will try and keep the explanation as simple as I can.

First of all, I need to introduce a tiny bit of calculus. One way to look at calculus is to find the gradient of a curve at a specific value. Hence, in order to make two graphs to connect smoothly (useful when you draw wiggly lines) to achieve a shape you would otherwise be unable to (likely due to limit of knowledge in mathematics like me), you ensure that at your chosen point for connection, that the two graphs have the exact same gradient. This is called a smooth joint, but I call it mathematically smooth.

However, as I have zero intention of deriving and integrating every time I want to draw on Desmos, I just trial and error my equation by dilating and/or translating it to the chosen point where even though the graphs ends up intersect at at least 2 points, I ensure that the two intersect points are so close to the point of connection that you cannot tell it being not mathematically smooth with the naked eye, hence I named it visually smooth joints.

![](https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/9587c4c5-75a9-4862-b966-8fa63613a732.png align="center")

![](https://cdn.hashnode.com/uploads/covers/69ba1127c22d3eeb8a24feaf/2d394bfd-12eb-42eb-ab07-46ca464a4ea0.png align="center")

* * *

## 5\. My Art Workflow

*   Import image
    
*   Tracing using equations/relations and restrict using domain/range
    
*   Apply visually smooth joins throughout when needed
    
*   Save and share!
    

* * *

Thx for reading and best of luck!