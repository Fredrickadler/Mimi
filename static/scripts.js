
document.addEventListener("DOMContentLoaded", () => {
  const dashboard = document.getElementById("dashboard");

  // Fetch user data
  fetch("/api/user/1")
    .then(response => response.json())
    .then(user => {
      dashboard.innerHTML = `
        <div>
          <h2>Welcome, ${user.name}</h2>
          <p>Balance: ${user.balance}</p>
          <p>Energy: ${user.energy}%</p>
        </div>
      `;
    })
    .catch(err => console.error("Error fetching user data:", err));

  // Fetch blockchain stats
  fetch("/api/blockchain")
    .then(response => response.json())
    .then(stats => {
      const statsDiv = document.createElement("div");
      statsDiv.innerHTML = `
        <h2>Blockchain Stats</h2>
        <p>Total Mined: ${stats.total_mined}%</p>
        <p>Total Supply: ${stats.total_supply}</p>
        <p>Blocks Mined: ${stats.blocks_mined}</p>
      `;
      dashboard.appendChild(statsDiv);
    })
    .catch(err => console.error("Error fetching blockchain stats:", err));
});
