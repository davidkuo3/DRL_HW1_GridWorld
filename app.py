from flask import Flask, render_template, request, jsonify
import numpy as np
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json
    n = int(data['n'])
    start_pos = tuple(data['start'])
    end_pos = tuple(data['end'])
    obstacles = [tuple(o) for o in data['obstacles']]
    
    # 1. Generate random policy
    # 0: Up, 1: Down, 2: Left, 3: Right
    policy = np.random.randint(0, 4, (n, n))
    
    # 2. Policy Evaluation
    gamma = 0.95
    threshold = 1e-4
    V = np.zeros((n, n))
    
    # Reward function: -1 per step, Goal is 0 and absorbing
    # Obstacles are non-passable (stay in place)
    
    max_iter = 1000
    for _ in range(max_iter):
        delta = 0
        new_V = np.copy(V)
        for r in range(n):
            for c in range(n):
                # Goal state
                if (r, c) == end_pos:
                    continue
                # Obstacle
                if (r, c) in obstacles:
                    continue
                
                old_v = V[r, c]
                action = policy[r, c]
                
                # Determine next state
                next_r, next_c = r, c
                if action == 0: next_r = max(0, r - 1)      # Up
                elif action == 1: next_r = min(n - 1, r + 1) # Down
                elif action == 2: next_c = max(0, c - 1)      # Left
                elif action == 3: next_c = min(n - 1, c + 1) # Right
                
                # If next state is an obstacle, stay in place
                if (next_r, next_c) in obstacles:
                    next_r, next_c = r, c
                
                reward = -1
                new_V[r, c] = reward + gamma * V[next_r, next_c]
                delta = max(delta, abs(old_v - new_V[r, c]))
        
        V = new_V
        if delta < threshold:
            break
            
    # Prepare result for JS
    # Convert numpy types to python native types for JSON
    res_values = V.tolist()
    res_policy = policy.tolist()
    
    return jsonify({
        'values': res_values,
        'policy': res_policy
    })

import os

if __name__ == '__main__':
    # Use PORT provided by cloud environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
