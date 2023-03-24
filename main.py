from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
  @import url("https://fonts.googleapis.com/css2?family=Silkscreen&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;1,400&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap");

/* Global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html {
  font-family: "Rubik", sans-serif;
  color: var(--black);
  scroll-behavior: smooth;
}
li, a, button {
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-size: 1rem;
  color: var(--font-color1);
  text-decoration: none;
}
body {
  overflow-x: hidden !important;
}
.hidden {
  display: none !important;
}
/* Variables */
.search-container {
  width: auto;
  margin-top: -85px;
  margin-left: 140px;
  margin-bottom: 10px;
  height: 50px;
  border-radius: 25px;
}
.logo {
  width: auto;
  margin: -10px;
  margin-left: 10px;
  height: 100px;
  margin-bottom: 20px;
}
.search-container2 {
  width: auto;
  margin: -0px;
  margin-left: 900px;
  height: 100px;
}
input[type="text"] {
  display: block;
  width: calc(25% - 24px); /*20px [ left & Right ] padding + 4px border [ left & Right ] */ 
  font-size: 18px;
  font-weight: 600;
  color: black;
  padding: 10px;
  padding-left: 10px;
  padding-right: 10px;
  border: 2px solid black;
}

.darksection {
  background-color: lightblue;
  color: lightblue;
}
#loader {
  border: 12px solid #f3f3f3;
  border-radius: 50%;
  border-top: 12px solid #444444;
  width: 70px;
  height: 70px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  100% {
      transform: rotate(360deg);
  }
}

.center {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
}
  </style>
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
    }

    td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }
    
    tr:nth-child(odd) {
      background-color: rgb(255, 255, 255);
    }

    tr:nth-child(even) {
      background-color: lightblue;
    }

    .masked {
      text-overflow: ellipsis;
      overflow: hidden;
      white-space: nowrap;
      width: 150px;
    }
  </style>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <link rel="stylesheet" href="assets/style.css" />
</head>
<body>
  <div id="loader" class="center"></div>  
  <img src="https://i.ibb.co/DQzNLqR/Metazord-Logo.png"  class="logo" />
  <input type="text" id="searchInput" class="search-container" placeholder="Search for opportunities or contacts..."> 
  <table id="dataTable">
    <tr>
      <th>Opportunity Name</th>
      <th>Opportunity Description</th>
      <th>Opportunity Close Date</th>
      <th>Associated Account Name</th>
      <th>Name of Most Recent Contact</th>
      <th>Contact gmail</th>
      <th>Contact Number</th>
    </tr>
    <tr>
      <td>Information Technology (IT)</td>
      <td class="masked">Software development, Web development, Data analysis, Cybersecurity. </td>
      <td>2023-02-15</td>
      <td>Abilash</td>
      <td>Aakash</td>
      <td class="masked">aakash11@gmail.com</td>
      <td class="masked">(256) 345-5698</td>
    </tr>
    <tr>
      <td>Business and finance</td>
      <td class="masked">Marketing, Sales, Human Resources, Accounting. </td>
      <td>2023-02-28</td>
      <td>Arun Raj</td>
      <td>Anjali</td>
      <td class="masked">anjali826@gmail.com</td>
      <td class="masked">(227) 569-7854</td>
    </tr>
    <tr>
        <td>Healthcare</td>
        <td class="masked">Nursing, Medical assisting, Physiotheraphist.</td>
        <td>2023-03-03</td>
        <td>Akshaya</td>
        <td>Anagha</td>
        <td class="masked">Anagha562@gmail.com</td>
        <td class="masked">(569) 789-6532</td>
      </tr>
      <tr>
        <td>Mechanical Engineering </td>
        <td class="masked">Product Design Engineer, Tools Engineer, Production Engineer, Quality Assurance.</td>
        <td>2023-03-05</td>
        <td>Bawanth</td>
        <td>Deepak</td>
        <td class="masked">deepakrj56@gmail.com</td>
        <td class="masked">(325) 365-8654</td>
      </tr>
      <tr>
        <td>Customer service</td>
        <td class="masked">Support, Call center, Executive, Representative, Manager.</td>
        <td>2023-02-14</td>
        <td>Santhosh</td>
        <td>Raghul Rawat</td>
        <td class="masked">rrawat5602@gmail.com</td>
        <td class="masked">(453) 365-7412</td>
      </tr>
      <tr>
        <td>Retail and sales</td>
        <td class="masked">Store management, merchandising, Marketting Associate. </td>
        <td>2023-03-12</td>
        <td>Roshni</td>
        <td>Pawan Reddy</td>
        <td class="masked">reddypawan690@gmail.com</td>
        <td class="masked">(354) 451-6893</td>
      </tr>
      <tr>
        <td>Media and communication</td>
        <td class="masked"> Journalism, Public relations,News Readers, Reporters .</td>
        <td>2023-03-10</td>
        <td>Mythili</td>
        <td>Arun Kumar</td>
        <td class="masked">arun22@gmail.com</td>
        <td class="masked">(456) 256-9832</td>
      </tr>
      <tr>
        <td>Education</td>
        <td class="masked"> Maths, Physics, Chemistry, Accounts,Economics, Computer Lab assistant .</td>
        <td>2023-04-15</td>
        <td>Paramasivam</td>
        <td>Devaraj</td>
        <td class="masked">devaraj16@gmail.com</td>
        <td class="masked">(563) 126-9234</td>
      </tr>
      <tr>
        <td>Civil Engineering</td>
        <td class="masked">Site Management, Project Management, Fire risk assessor, Quantity Surveyor.</td>
        <td>2023-05-20</td>
        <td>Bala Vignesh</td>
        <td>Christopher</td>
        <td class="masked">christopheraaro3@gmail.com</td>
        <td class="masked">(564) 267-9423</td>
      </tr>
      <tr>
        <td>Transportation</td>
        <td class="masked">Truck Driver, Taxi Driver, Heavy Loader, Logistics.</td>
        <td>2023-06-05</td>
        <td>Siranjivi</td>
        <td>Kanchana</td>
        <td class="masked">kanchana69@gmail.com</td>
        <td class="masked">(654) 364-8961</td>
      </tr>
      <tr>
        <td>Science and research</td>
        <td class="masked">laboratory research, scientific writing.</td>
        <td>2023-05-14</td>
        <td>Pooja</td>
        <td>Ragubathi</td>
        <td class="masked">raagupathi56@gmail.com</td>
        <td class="masked">(563) 324-8963</td>
      </tr>
      <tr>
        <td>Government and public sector</td>
        <td class="masked">Administrative, Policy analysis, Accountant, Clerk.</td>
        <td>2023-06-03</td>
        <td>Nazreen</td>
        <td>Shanmugan</td>
        <td class="masked">shans23@gmail.com</td>
        <td class="masked">(783) 451-9864</td>
      </tr>
      <tr>
        <td>Digital Marketing</td>
        <td class="masked">Graphic design, Digital media, Photography, Content Writer.</td>
        <td>2023-06-25</td>
        <td>Harini</td>
        <td>Rahul</td>
        <td class="masked">rahul23@gmail.com</td>
        <td class="masked">(365) 994-2328</td>
      </tr>
  </table>
  <script>
    $(document).ready(function() {
      $("#searchInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#dataTable tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      });
    });
  </script>
  <script>
    document.onreadystatechange = function() {
        if (document.readyState !== "complete") {
            document.querySelector(
            "body").style.visibility = "hidden";
            document.querySelector(
            "#loader").style.visibility = "visible";
        } else {
            document.querySelector(
            "#loader").style.display = "none";
            document.querySelector(
            "body").style.visibility = "visible";
        }
    };
</script>
</body>
</html>

    '''

if __name__ == "__main__":
    app.run(host= os.getenv('IP',"0.0.0.0"), port=int(os.getenv('PORT',5005)))