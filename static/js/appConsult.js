function consult_user() {
    let id = document.getElementById("ident").value;
    let obj_data = {
        "id": id
    };
    fetch("/consult_user", {
        "method": "post",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(obj_data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status == "ok") {
            document.getElementById("txt-name").value = data.name + "\n";
            document.getElementById("txt-lastname").value = data.lastname;
            document.getElementById("txt-birthday").value = data.birthday;
            let imgUrl = "http://bucket-cristian-ovalles-cymetria.s3-website.us-east-2.amazonaws.com/images/" + id + ".png";
            console.log("Image URL: " + imgUrl);
            document.getElementById("img-user").src = imgUrl;
        } else {
            alert("Usuario no encontrado");
        }
    })
    .catch(err => alert(err));
}