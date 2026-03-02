# 🏃‍♂️ DUDE RUNNER - Project Report (v2.0)

## 1. Introduction
**Dude Runner** is a high-octane, web-based endless runner game built using the **Phaser 3** framework. Originally featuring a single hero in a Chennai-themed environment, the game has evolved into a feature-rich experience with multiple characters, a simultaneous two-player mode, and full mobile support.

---

## 2. 🚀 Latest Progress (v2.0 Update)
Since the initial release, several major milestones have been achieved:

- ✅ **Two-Player Mode**: Play side-by-side with a friend! Hero (Agan) and Mamitha (Kural) can now run together in a shared-screen cooperative experience.
- ✅ **Character Selection**: In Single Player mode, choose between **AGAN (Hero)** or **KURAL (Mamitha)**.
- ✅ **New Character: Kural (Mamitha)**: A fully animated red-shirt heroine with unique "arms-raised" jump and sitting death poses.
- ✅ **Death Animations**: Added custom "hit" frames for both characters (Row 3 of sprite sheets) providing visual feedback on collision.
- ✅ **Mobile Optimization**: Added on-screen touch controls, a dedicated Pause button, and a comprehensive [Mobile Build Guide](MOBILE_GUIDE.md).
- ✅ **Visual Polish**: Integrated camera shake on collision, screen flashes for level transitions, and refined menu screens.
- ✅ **Performance**: Normalized sprite sheets (1756x1756) resulting in an **84% reduction** in file size (from 6.27MB to 1.00MB).

---

## 3. Project Structure
The project follows a modular structure with several specialized documentation files and utility scripts:

```
duderunner/
│
├── index.html                # MAIN ENTRY POINT: Game Logic & Scene Management
├── play_game.bat             # Launcher script (bypass CORS issues)
├── README.md                 # Main Project Report
│
├── assets/                   # Visual Assets (Backgrounds, Obstacles, Mangoes)
│   ├── hero_sheet_normalized.png    # Agan (P1) animation sheet
│   └── mamitha_sheet_normalized.png # Kural (P2) animation sheet
│
├── audio/                    # Sound Effects & Music (mp3)
│
├── CHARACTER_SELECTION.md    # Guide for choosing heroes
├── TWO_PLAYER_MODE.md        # Guide for simultaneous gameplay
├── DEATH_ANIMATION.md        # Documentation for hit animations
├── MOBILE_GUIDE.md           # Instructions for APK building
├── FINAL_FIXES.md            # Technical resolution log
│
└── normalize_*.py            # Python scripts for asset optimization
```

---

## 4. 🎮 Controls

### **Desktop (Keyboard)**
| Action | Player 1 (Agan) | Player 2 (Kural) |
| :--- | :--- | :--- |
| **Jump** | **W** or **SPACE** | **↑ UP ARROW** |
| **Pause** | **ESC** | **ESC** |

### **Mobile (Touch)**
- **Single Player**: Tap anywhere to jump.
- **Two Player**: Tap **Left Side** for P1, **Right Side** for P2.
- **UI**: Dedicated **"II" button** in the top-right to pause.

---

## 5. Game Flow & Mechanics

### **Phase 1: Game Setup**
1. **Player Mode Select**: Choose between 1 Player or 2 Players.
2. **Character Select (1P Only)**: Choose your hero (Agan or Kural).
3. **Difficulty Select**: Choose from Beginner, Medium, Hard, or God Mode.

### **Phase 2: Gameplay & Progression**
- **Infinite Run**: Characters run through level 1 (Day) and transition to level 2 (Sunset) after **2500m**.
- **Shared Scoring**: In 2-Player mode, both players contribute to the same score and mango count.
- **Team Survival**: If *either* player hits an obstacle, it's Game Over for both! Coordinate your jumps to survive.

### **Phase 3: Collision & Game Over**
- **Death Pose**: Characters transition to a sitting "hit" frame upon collision.
- **Feedback**: Camera shakes and a 500ms delay allow players to see the impact before the Game Over screen appears.

---

## 6. Technical Implementation Details
- **Engine**: Phaser 3 (Arcade Physics).
- **Sprite Normalization**: All character frames are centered in 439x878 slots within a 1756x1756 texture for consistent hitboxes and animations.
- **Dynamic Loading**: Player 2 is instantiated dynamically only when 2-Player mode is selected to optimize memory.
- **Render Depth**: Hero (Depth 10) is slightly ahead (X: 150), while Mamitha (Depth 9) is slightly behind (X: 120) to ensure both are visible.

---

## 7. How to Run
Due to browser security policies (CORS), run the game via a local server:

1.  Double-click `play_game.bat`.
2.  Or open the folder with VS Code **Live Server**.
3.  Access via `http://localhost:8000`.

---
*Last Updated: 2026-03-03*
*Developed by Kumaresa Pandiyan & Antigravity Agent*

