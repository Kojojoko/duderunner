# 📁 DUDE RUNNER - Project Structure (Actual)

This document provides a complete map of the current project directory, showing all files and subdirectories as they are organized on disk.

## 🏗️ Root Directory

```
C:\Users\Kumaresa pandiyan\OneDrive\Documents\duderunner\
│
├── 🎮 Core Game Files
│   ├── index.html                # MAIN ENTRY POINT: Phaser 3 logic
│   ├── play_game.bat             # Launcher script (Server + Browser)
│   ├── README.md                 # Main Project Report
│   ├── PROJECT_STRUCTURE.md      # This document
│   ├── manifest.json             # Web App Manifest
│   └── sw.js                     # Service Worker
│
├── 📝 Feature Documentation
│   ├── CHARACTER_SELECTION.md
│   ├── CORRECTIONS.md
│   ├── DEATH_ANIMATION.md
│   ├── FINAL_FIXES.md
│   ├── FRAME_CLIPPING_FIXED.md
│   ├── HERO_SPRITE_FIXED.md
│   ├── MAMITHA_NORMALIZATION.md
│   ├── MOBILE_GUIDE.md
│   ├── QUICKSTART.md
│   └── TWO_PLAYER_MODE.md
│
├── � Optimization & Analysis Scripts
│   ├── normalize_hero_sheet.py
│   ├── normalize_mamitha_sheet.py
│   ├── normalize_sheet.py
│   ├── optimize_level2.py
│   ├── optimize_logo.py
│   ├── analyze_sheet.py
│   ├── analyze_mamitha_sheet.py
│   ├── analyze_pradeep_sheet.py
│   ├── analyze_row1.py
│   ├── analyze_row2.py
│   ├── analyze_sheet_y.py
│   ├── create_comparison.py
│   └── debug_hero_sheet.py
│
├── 🖼️ assets/                    # Main game visual assets
│   ├── bg_ground.png, bg_sky.png...
│   ├── hero_sheet_normalized.png
│   ├── mamitha_sheet_normalized.png
│   ├── obstacle_*.png (metro, car, bike)
│   ├── logo.png, icon.png
│   └── mango.png (collectible)
│
├── 🎵 audio/                     # Game soundtracks & SFX
│   ├── bg_audio.mp3 (Level 1)
│   ├── bg2.mp3 (Level 2)
│   ├── jump.mp3
│   └── game-over.mp3
│
└── 📂 duderunner/                # Nested project subdirectory
    ├── assets/                   # Sub-project assets
    ├── audio/                    # Sub-project audio
    └── index.html, README.md...  # Sub-project core files
```

## 📄 Summary of Top-Level Folders

### 1. Root Folder
Contains the main `index.html` and a flat list of development scripts and documentation. Most logic has migrated to these files.

### 2. `assets/`
Contains the normalized sprites and optimized backgrounds. The characters use `hero_sheet_normalized.png` and `mamitha_sheet_normalized.png` for consistent animations.

### 3. `audio/`
Hosts the MP3 files for the Chennai-themed levels and sound effects.

### 4. `duderunner/` (Subdirectory)
Appears to be a separate backup or previous version of the project containing its own assets and logic files.

### 5. `assets_backup/`
A preservation directory containing original obstacle and background assets before optimization.

---
*Updated: 2026-03-03*

