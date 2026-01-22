# Snake Game 🐍

## Overview
A classic Snake game implemented in Python using the built-in `turtle` graphics library.  
The player controls the snake using keyboard inputs, eats food to grow longer, and avoids collisions with walls or itself.

This project demonstrates object-oriented programming, event handling, and real-time game loops in Python.

---

## Problem Statement
The Snake game is a well-known arcade game that requires continuous movement, collision detection, and state management.  
The goal of this project is to recreate the game logic using Python without external game engines.

---

## Solution
The game is built using modular classes:
- `Snake` handles movement and body growth
- `Food` randomly spawns consumable items
- `Scoreboard` manages score tracking and game-over display

The main game loop updates the screen continuously while listening for user input.

---

## Features
- Keyboard-controlled snake movement
- Real-time collision detection
- Dynamic snake growth
- Random food spawning
- Score tracking
- Game-over detection
- Smooth animation using screen updates

---

## Tech Stack
- **Language:** Python
- **Graphics Library:** `turtle`
- **Concepts Used:** OOP, event-driven programming, game loops

---

## Controls
- **Up Arrow:** Move up  
- **Down Arrow:** Move down  
- **Left Arrow:** Move left  
- **Right Arrow:** Move right  

---

## Project Structure
```text
Snake-game/
│
├── main.py          # Main game loop
├── snake.py         # Snake movement and growth logic
├── food.py          # Food spawning logic
├── scoreboard.py   # Score display and game-over logic
