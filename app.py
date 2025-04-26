from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home(): 
    result = ""
    current_direction = request.form.get("current_direction", "to_12")

    if request.method == "POST":

        if "swap" in request.form:
            if current_direction == "to_12":
                current_direction = "to_24"  
            elif current_direction == "to_24":
                current_direction = "to_12"
             

        elif "convert" in request.form: 
            if current_direction == "to_12":
                time_24 = request.form["time_24"].strip()
                hour = int(time_24.split(":")[0])
                minute = int(time_24.split(":")[1])
                if hour == 00:
                     newhour = 12
                     period = "AM"

                elif hour >= 1 and hour <=11:
                    newhour = hour
                    period = "AM"

                elif hour == 12:
                    newhour = 12
                    period = "PM"

                elif hour >= 13 and hour <=23:
                    newhour = hour-12
                    period = "PM"

                result = f"{newhour}:{minute} {period}"
                
    
            elif current_direction == "to_24":
                time_12 = request.form["time_12"].strip()
                period = request.form["period"]
                hour2 = int(time_12.split(":")[0])
                minute2 = int(time_12.split(":")[1])
                
                if period == "AM" and hour2 == 12:
                    newhour2 = 0
    
                elif period == "AM" and hour2 != 12:
                    newhour2 = hour2
    
                elif period == "PM" and hour2 == 12:
                    newhour2 = 12
    
                elif period == "PM" and hour2 != 12:
                    newhour2 = hour2 + 12
    
                result = f"{newhour2}:{minute2}"
        
                          

    return render_template("index.html", result=result, direction = current_direction)

if __name__ == "__main__":
    app.run(debug=True)

