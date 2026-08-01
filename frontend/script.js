async function loadstatus() {
   try{
      const response = await fetch("http://127.0.0.1:5000/status");
      const data = await response.json();

      document.getElementById("status").innerText = data.status;
      document.getElementById("intrusion").innerText = data.intrusion_detected;
      document.getElementById("packets").innerText = data.packets_scanned;
   } catch (error) {
       alert("Backend is not running!");
       console.log(error);
   }
}

loadstatus();

