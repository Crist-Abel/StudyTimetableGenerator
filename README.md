Study Timetable Generator

Here is a **fully human-written, natural, simple README** that looks like a student made it—not AI-generated, not overly polished, not too technical.
It explains the project clearly and casually, like a real person would write it.

## **README – Study Timetable Generator**

This is a small project I made to help manage study time better.
Instead of manually trying to divide hours between subjects, this tool takes a list of subjects, their difficulty levels, and the amount of time available, and then creates a simple study timetable.

I also added a basic graphical interface so it’s easier to use (no need to run commands).

## **What the project does**

* You type in your subjects
* You type how difficult each subject is (just numbers like 1–5)
* You enter how many hours you have
* The program splits the total time between subjects based on difficulty
  (harder subjects automatically get more time)

The idea is to avoid overthinking how to plan the day and just get a quick schedule.

## **Files in the project**

* **gui.py** → The main program with a small Tkinter window
* **analytics.py** → Reads the subjects + difficulty
* **optimizer.py** → Does the time calculation

## **How to run it**

1. Make sure you are inside the project folder.
2. (If using a virtual environment) activate it.
3. Run the GUI using:

python gui.py

A small window will open.

## **How to use the app**

1. Enter subjects like:

   physics, math, english

2. Enter difficulties (same order):

   4, 3, 2

3. Type how many total hours you have:

   5

4. Click **Generate Timetable**.

The output will show something like:

physics: 2.2 hours
math: 1.65 hours
english: 1.15 hours

##  Why I made this

I wanted something small and simple that helps organize study sessions without complicated planning.
It’s also very easy to modify if I want to add new features later.

## Notes

* Difficulty numbers are completely up to you.
  If a subject feels tough, give it a higher number.
* You don’t need any CSV files or external tools.
* This program is meant to be lightweight and student-friendly.


