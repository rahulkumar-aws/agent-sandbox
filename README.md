# Agent Sandbox

A deterministic AI agent framework built entirely from first principles in Python. This repository strips away heavyweight frameworks to demonstrate the fundamental cybernetic mechanics of an autonomous agent: the ReAct (Reasoning + Acting) loop. 

## Overview
This project explicitly decouples the reasoning engine from the environment and tools, providing a clean foundation before introducing an LLM. It features a multi-room text-based environment where the agent must explore, manage its inventory, and achieve explicit goals.

## Repository Structure

* **`src/agent_sandbox/agent/`**: The core agent logic. Contains the agent's internal memory buffer (`state.py`), the deterministic decision-making policy (`policy.py`), and the termination evaluation (`agent.py`).
* **`src/agent_sandbox/environment/`**: Defines the physical ground truth (`world.py`), featuring a deterministic 3-room simulation (Hall, Kitchen, Study).
* **`src/agent_sandbox/tools/`**: Houses the action effectors (`actions.py`) that safely mutate the environment upon the agent's request[cite: 1].
* **`src/agent_sandbox/runtime/`**: The orchestrator (`runner.py`) that manages the continuous Observe -> Decide -> Act execution loop and evaluates task success within a Sandbox harness[cite: 1].
* **`examples/`**: Runnable evaluation scripts demonstrating the agent attempting specific tasks.

## Quick Start

Run the deterministic agent against the primary evaluation task ("Get the Treasure"):

```bash
export PYTHONPATH=./src
python examples/01_deterministic_agent.py