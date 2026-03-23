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
    algorithm = data.get('algorithm', 'policy_evaluation')
    
    gamma = 0.95
    threshold = 1e-4
    max_iter = 1000
    
    # 0: Up, 1: Down, 2: Left, 3: Right
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    V = np.zeros((n, n))
    policy = np.zeros((n, n), dtype=int)
    
    if algorithm == 'policy_evaluation':
        # 1. Generate random policy
        policy = np.random.randint(0, 4, (n, n))
        
        # 2. Policy Evaluation
        for _ in range(max_iter):
            delta = 0
            new_V = np.copy(V)
            for r in range(n):
                for c in range(n):
                    if (r, c) == end_pos or (r, c) in obstacles:
                        continue
                    
                    old_v = V[r, c]
                    action_idx = policy[r, c]
                    dr, dc = actions[action_idx]
                    
                    next_r, next_c = r + dr, c + dc
                    
                    # Boundary check and obstacle check
                    if not (0 <= next_r < n and 0 <= next_c < n) or (next_r, next_c) in obstacles:
                        next_r, next_c = r, c
                    
                    reward = -1
                    new_V[r, c] = reward + gamma * V[next_r, next_c]
                    delta = max(delta, abs(old_v - new_V[r, c]))
            
            V = new_V
            if delta < threshold:
                break
                
    elif algorithm == 'value_iteration':
        # 1. Value Iteration
        for _ in range(max_iter):
            delta = 0
            new_V = np.copy(V)
            for r in range(n):
                for c in range(n):
                    if (r, c) == end_pos or (r, c) in obstacles:
                        continue
                    
                    old_v = V[r, c]
                    action_values = []
                    
                    for action_idx in range(4):
                        dr, dc = actions[action_idx]
                        next_r, next_c = r + dr, c + dc
                        
                        if not (0 <= next_r < n and 0 <= next_c < n) or (next_r, next_c) in obstacles:
                            next_r, next_c = r, c
                        
                        reward = -1
                        action_values.append(reward + gamma * V[next_r, next_c])
                    
                    new_V[r, c] = max(action_values)
                    delta = max(delta, abs(old_v - new_V[r, c]))
            
            V = new_V
            if delta < threshold:
                break
        
        # 2. Derive Optimal Policy
        for r in range(n):
            for c in range(n):
                if (r, c) == end_pos or (r, c) in obstacles:
                    continue
                
                action_values = []
                for action_idx in range(4):
                    dr, dc = actions[action_idx]
                    next_r, next_c = r + dr, c + dc
                    
                    if not (0 <= next_r < n and 0 <= next_c < n) or (next_r, next_c) in obstacles:
                        next_r, next_c = r, c
                    
                    action_values.append(-1 + gamma * V[next_r, next_c])
                
                policy[r, c] = np.argmax(action_values)

    return jsonify({
        'values': V.tolist(),
        'policy': policy.tolist()
    })

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
