# BattleshipPYQT5
# Battleship Game (Network Multiplayer)

A Python implementation of Battleship with client-server architecture, supporting two-player competitive gameplay over a network.

## Features
- **Network multiplayer** (LAN play supported)
- **Text-based interface** with clean output
- **Role-based gameplay** (Captain vs. General)
- **Auto-generated ship layouts**
- **Detailed game logs** for debugging

## Requirements
- Python 3.6+
- PyQt5 (for client GUI components)


## How to Run
1. **Start the Server** (Host Machine):   
    Server waits for 2 players on port 12345 (configurable in GameIni.py).
2. **Launch Clients** (Same or Different Machines):
- Enter server IP when prompted (use 'localhost' for local play)

3. **Game Flow**:
- Server assigns random roles (Captain/General)
- Players take turns entering coordinates
- Game continues until all ships are sunk

## Game Rules
### Board Setup
- 6×6 grid
- 5 ships (each 2 tiles long)
- Random placement at game start

### Gameplay
1. Alternate turns between players
2. Enter moves as `row,col` (e.g., `2,3`)
3. Feedback:
   - Uppercase `C`/`G`: Hit
   - Lowercase `c`/`g`: Miss

### Roles & Scoring
- **Captain (C)**: +1 per hit on ship segment
- **General (G)**: +2 per sunk ship

### Winning
- First to 10 hits wins
- Tiebreaker: Highest role score

## Troubleshooting
- **Connection issues**: Verify server IP and firewall
- **Port conflicts**: Change PORT in GameIni.py
- **PyQt5 errors**: Try `pip install --force-reinstall PyQt5`
- **Game freeze**: Check BattleShipGameServer.log
## Disclaimer
This implementation is functional but not perfect. Several areas could be improved:
- Error handling for network disconnections
- Input validation for client commands
- Game state recovery options
- Additional unit tests
- The code serves as a working foundation that can be enhanced for production use.
## Authors
- Israel Prusente 
- Joseph Duda 
