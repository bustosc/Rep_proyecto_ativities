function consult_activity() {
    let activity_id = document.getElementById('activity_id').value;
    fetch('/consult_activity', {
        method: "post",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(activity_id)
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.error) {
            document.getElementById("txt-response").value = data.error;
        } else {
            document.getElementById("txt-response").value = data.activity_name + " - " + data.description;
            document.getElementById("img-response").src = data.image_url;
        }
    })
}