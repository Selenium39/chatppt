// Function to show the modal
function showModal() {
    document.getElementById("tip").innerHTML = "正在生成您的演示文稿...";
    var modal = document.getElementById('modal-generate');
    modal.style.display = 'block';
}

// Function to hide the modal
function hideModal() {
    var modal = document.getElementById('modal-generate');
    modal.style.display = 'none';
}

function showDownload() {
    document.getElementById("tip").innerHTML = "您的演示文稿已完成。";
    var download = document.getElementById('download');
    download.style.display = 'block';
}

function hideDownload() {
    var download = document.getElementById('download');
    download.style.display = 'none';
}

// Event listener for the "Generate" button
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('downloadLink').addEventListener('click', function (e) {
        hideDownload()
        hideModal()
    })
    document.getElementById('generate-button').addEventListener('click', function (e) {
        e.preventDefault();  // Prevent the default form submission
        showModal();  // Show the modal


        // Serialize form data and send it to the server via an AJAX POST request
        const formData = new FormData();
        formData.append('presentation_title', document.getElementById('presentation_title').value);
        formData.append('presenter_name', document.getElementById('presenter_name').value);
        formData.append('number_of_slide', document.getElementById('number_of_slide').value);
        formData.append('user_text', document.getElementById('user_text').value);
        formData.append('insert_image', document.getElementById('insert_image').checked);

        const template_choice = document.querySelector('input[name="template_choice"]:checked').value;
        formData.append('template_choice', template_choice);
        // ... append other form data similarly
        console.log([...formData]);  // Check the logged output to ensure the data is correct
        fetch('/generator', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response
            })
            .then(response => response.json())
            .then(data => {
                if (data.filename) {
                    console.log(data.filename)
                    document.getElementById('downloadLink').href = `/download/${data.filename}`;
                    showDownload();
                } else if (data.error) {
                    console.error('Error generating file:', data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});


