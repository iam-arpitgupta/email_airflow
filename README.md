# Airflow Agentic Workflows

This project integrates Apache Airflow with LangGraph to create agentic workflows. It leverages Airflow for orchestration and scheduling, while LangGraph manages the stateful agent interactions.

## Project Structure

- **`dags/`**: Contains Airflow DAGs (Directed Acyclic Graphs).
  - `agentic_email_dag.py`: The main DAG defining the agentic workflow.
- **`include/`**: Helper modules and resources.
  - **`agents/`**: Contains the LangGraph agent definitions.
    - `graph.py`: Defines the graph structure (nodes and edges).
    - `nodes.py`: Contains the logic for each node in the graph.
    - `state.py`: Defines the state schema for the graph.
  - **`scripts/`**: Utility scripts.
    - `utils.py`: Helper functions.
- **`docker-compose.yaml`**: (Optional) Configuration for running Airflow in Docker.

## Prerequisites

- **Python**: version 3.11 or higher
- **pip**: Python package installer

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd airflow
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   - Create a `.env` file in the root directory if needed (see `.env.example` if available).

## Running the Project

### Local Development (Standalone)

To run the agent logic independently of Airflow for testing:

```bash
python main.py
```

### Running with Airflow

1. **Initialize Airflow Database:**
   ```bash
   export AIRFLOW_HOME=$(pwd)
   airflow db init
   ```

2. **Create an Admin User:**
   ```bash
   airflow users create \
       --username admin \
       --firstname Admin \
       --lastname User \
       --role Admin \
       --email admin@example.com
   ```

3. **Start the Scheduler:**
   ```bash
   airflow scheduler
   ```

4. **Start the Webserver (in a new terminal):**
   ```bash
   airflow webserver --port 8080
   ```

5. **Access the UI:**
   Open [http://localhost:8080](http://localhost:8080) and login with the credentials created above.
