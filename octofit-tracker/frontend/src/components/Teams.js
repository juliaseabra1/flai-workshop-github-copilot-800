import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
        console.log('Fetching teams from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Teams data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(teamsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching teams:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return <div className="container mt-4 loading-container"><h2>Loading teams...</h2></div>;
  if (error) return <div className="container mt-4 error-container"><h2>Error: {error}</h2></div>;

  return (
    <div className="container mt-4">
      <h2>👥 Teams</h2>
      <p className="lead">Join a team and compete together!</p>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Team Name</th>
              <th>Members</th>
              <th>Member Count</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team) => (
              <tr key={team.id}>
                <td><strong>{team.name}</strong></td>
                <td>{team.members && team.members.length > 0 ? team.members.join(', ') : <span className="text-muted">No members</span>}</td>
                <td><span className="badge bg-primary">{team.members ? team.members.length : 0}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Teams;
