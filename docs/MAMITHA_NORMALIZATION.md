# Mamitha Sheet Normalization - Summary

## Overview
Successfully normalized the `mamitha_sheet.png` for use in the two-player game mode.

## Processing Details

### Input
- **File**: `mamitha_sheet.png`
- **Size**: 1536x2752 pixels
- **File Size**: 6.27 MB
- **Structure**: 3 rows with 9 total frames

### Output
- **File**: `mamitha_sheet_normalized.png`
- **Size**: 1756x1756 pixels
- **File Size**: 1.34 MB
- **Reduction**: 78.6% smaller
- **Structure**: 
  - Row 1: 4 running frames @ 439x878 each
  - Row 2: 1 jump frame @ 439x878 (centered)

## Frame Coordinates

The normalized spritesheet uses the same layout as `hero_sheet_normalized.png`:

```
run0: x=0,    y=0   (frame 439x878)
run1: x=439,  y=0   (frame 439x878)  
run2: x=878,  y=0   (frame 439x878)
run3: x=1317, y=0   (frame 439x878)
jump: x=658,  y=878 (frame 439x878, centered)
```

## Usage in Game

To use the mamitha character in your Phaser game, follow the same pattern as the hero:

1. **Preload** (in `preload()` function):
```javascript
this.load.image('mamitha_sheet', 'assets/mamitha_sheet_normalized.png');
```

2. **Create Atlas** (in `create()` function):
```javascript
const mamithaSheet = this.textures.get('mamitha_sheet');
mamithaSheet.add('run0', 0, 0, 0, 439, 878);
mamithaSheet.add('run1', 0, 439, 0, 439, 878);
mamithaSheet.add('run2', 0, 878, 0, 439, 878);
mamithaSheet.add('run3', 0, 1317, 0, 439, 878);
mamithaSheet.add('jump', 0, 658, 878, 439, 878);
```

3. **Create Animations**:
```javascript
this.anims.create({
    key: 'mamitha_run',
    frames: [
        { key: 'mamitha_sheet', frame: 'run0' },
        { key: 'mamitha_sheet', frame: 'run1' },
        { key: 'mamitha_sheet', frame: 'run2' },
        { key: 'mamitha_sheet', frame: 'run3' }
    ],
    frameRate: 10,
    repeat: -1
});

this.anims.create({
    key: 'mamitha_jump',
    frames: [{ key: 'mamitha_sheet', frame: 'jump' }],
    frameRate: 10
});
```

4. **Create Player Sprite**:
```javascript
mamitha = this.physics.add.sprite(CONFIG.heroX + 100, FLOOR_Y - 50, 'mamitha_sheet', 'run0');
mamitha.setOrigin(0.5, 1);
mamitha.setScale(CONFIG.heroScale); // Use same scale as hero (0.18)
mamitha.setDepth(10);
mamitha.play('mamitha_run');
```

## Comparison with Hero

Both characters now use identical dimensions and layout:
- **Frame size**: 439x878 pixels
- **Sheet size**: 1756x1756 pixels
- **Layout**: Same (4 run frames + 1 jump frame)
- **Scale in game**: 0.18 (from CONFIG.heroScale)

This ensures both characters appear at the same size and work seamlessly in two-player mode.

## Scripts Created

1. **normalize_mamitha_sheet.py** - Main normalization script
2. **analyze_mamitha_sheet.py** - Frame detection and analysis

## Next Steps

To implement two-player mode in the game:
1. Add player selection UI (1 player vs 2 player)
2. Load mamitha_sheet in preload
3. Create second player sprite when 2-player mode is selected
4. Duplicate input handling for second player (different keys)
5. Add collision detection for both players

---
*Generated: 2026-02-04*
