from flask import Flask, render_template_string, request

app = Flask(__𝗕𝗟𝗔𝗖𝗞 𝗣𝗔𝗡𝗧𝗛𝗘𝗥 𝗔𝗥𝗦 𝗕𝗥𝗔𝗡𝗗__)

# HTML Code (Embedded in Flask script)
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Offline WhatsApp Chat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            width: 400px;
            text-align: center;
        }
        .container h1 {
            margin-bottom: 20px;
            font-size: 22px;
            color: #333;
        }
        .container input, .container select, .container button {
            width: calc(100% - 20px);
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        .container button {
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        .container button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <button onclick="stopMessaging()" style="background-color: #007bff; color: white; border: none; cursor: pointer; padding: 10px; border-radius: 5px;">STOP MESSAGING</button>
        <h1>OFFLINE WHATSAPP CHAT</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="text" name="your_name" placeholder="Your Name" required>
            <input type="text" name="target_phone" placeholder="Target Phone Number" required>
            <select name="target_type" required>
                <option value="" disabled selected>Select Target Type</option>
                <option value="individual">Individual</option>
                <option value="group">Group</option>
            </select>
            <label>input creds.json</label>
            <input type="file" name="creds_file" accept=".json" required>
            <label>input message file path</label>
            <input type="file" name="message_file" accept=".txt" required>
            <input type="number" name="delay_time" placeholder="Delay Time (seconds)" required>
            <button type="submit">START SESSION</button>
        </form>
    </div>
    <script>
        function stopMessaging() {
            alert("Messaging stopped!");
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle form data
        your_name = request.form.get("your_name")
        target_phone = request.form.get("target_phone")
        target_type = request.form.get("target_type")
        creds_file = request.files.get("creds_file")
        message_file = request.files.get("message_file")
        delay_time = request.form.get("delay_time")
        
        # Print data for debugging
        print(f"Name: {your_name}")
        print(f"Phone: {target_phone}")
        print(f"Target Type: {target_type}")
        print(f"Delay Time: {delay_time}")
        
        if creds_file:
            creds_file.save(f"./{creds_file.filename}")
            print(f"Saved creds.json: {creds_file.filename}")
        
        if message_file:
            message_file.save(f"./{message_file.filename}")
            print(f"Saved message file: {message_file.filename}")
        
        return "Session Started! Check server logs for details."
    
    return render_template_string(html_code)

if __name__ == "__main__":
    # Flask app runs on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)