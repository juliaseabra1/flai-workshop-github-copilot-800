import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(workoutsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4 loading-container"><h2>Loading workouts...</h2></div>;
  if (error) return <div className="container mt-4 error-container"><h2>Error: {error}</h2></div>;

  return (
    <div className="container mt-4">
      <h2>💪 Workout Library</h2>
      <p className="lead">Discover personalized workout suggestions</p>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Workout Name</th>
              <th>Description</th>
              <th>Difficulty</th>
              <th>Duration (min)</th>
              <th>Calories Target</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout) => (
              <tr key={workout.id}>
                <td><strong>{workout.name}</strong></td>
                <td>{workout.description}</td>
                <td><span className="badge bg-info">{workout.difficulty_level}</span></td>
                <td>{workout.duration_minutes}</td>
                <td>{workout.calories_target}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
