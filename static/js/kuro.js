const toggleLeft = document.getElementById('toggleLeft');
const toggleRight = document.getElementById('toggleRight');
const sidebarLeft = document.querySelector('.sidebar-left');
const sidebarRight = document.querySelector('.sidebar-right');
const overlay = document.getElementById('overlay');
const footer = document.getElementById('footer');
const arrowIcon = document.getElementById('arrowIcon');

toggleLeft.addEventListener('click', () => {
    sidebarLeft.classList.toggle('active');
    overlay.classList.toggle('active');
});

toggleRight.addEventListener('click', () => {
    sidebarRight.classList.toggle('active');
    overlay.classList.toggle('active');
});

overlay.addEventListener('click', () => {
    sidebarLeft.classList.remove('active');
    sidebarRight.classList.remove('active');
    overlay.classList.remove('active');
});

arrowIcon.addEventListener('click', () => {
    footer.classList.toggle('active');
    arrowIcon.classList.toggle('move-up');
    // Change the icon from arrow-up to arrow-down and vice versa
    const icon = arrowIcon.querySelector('i');
    if (arrowIcon.classList.contains('move-up')) {
        arrowIcon.classList.remove('move-bottom');
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    } else {
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    }
});

document.getElementById("emailLink").addEventListener("click", function() {
    window.location.href = "mailto:ryanoktaviandi1010@gmail.com";
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

function copyText(button) {
    // Get the adjacent <span> element containing the text
    var spanElement = button.querySelector("span.bg-gray-500");

    // Get the text content of the adjacent <span> element
    var currentURL = window.location.href;
    currentURL = currentURL.replace(/\/+$/, ''); // Remove trailing slashes
    var textContent = (spanElement.innerText || spanElement.textContent).replace(/^\/+/, ''); // Remove leading slashes

    // Concatenate current URL with the text content, ensuring only one slash between them
    var textToCopy = currentURL + "/" + textContent;

    // Copy the text to the clipboard
    navigator.clipboard.writeText(textToCopy)
        .then(function() {
            // Create a success alert with Tailwind and DaisyUI classes
            var alertDiv = document.createElement('div');
            alertDiv.className = 'bg-green-500 text-white px-2 py-1 rounded-lg flex items-center';
            alertDiv.setAttribute('role', 'alert');
            alertDiv.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span>Link has been copied!</span>
            `;
            document.getElementById('alertContainer').appendChild(alertDiv);

            // Remove the alert after 3 seconds
            setTimeout(function() {
                alertDiv.remove();
            }, 3000);
        })
        .catch(function(error) {
            console.error('Unable to copy:', error);
        });
}

var ItemDataHandler = (function() {
    function fetchData(url, elementId) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                if (xhr.status == 200) {
                    var jsonData = JSON.parse(xhr.responseText);
                    document.getElementById(elementId).innerText = JSON.stringify(jsonData, null, 4);
                    hideSpinner(elementId);
                } else {
                    console.error('Failed to fetch JSON data:', xhr.status);
                    hideSpinner(elementId);
                }
            }
        };
        xhr.open('GET', url);
        xhr.send();
        showSpinner(elementId);
    }

    function toggleItemData(elementId) {
        var itemDataDiv = document.getElementById(elementId);
        if (itemDataDiv.style.display === 'none') {
            itemDataDiv.style.display = 'block';
            fetchData(itemDataDiv.dataset.apiUrl, elementId);
        } else {
            itemDataDiv.style.display = 'none';
        }
    }

    function copyData(elementId) {
        var jsonData = document.getElementById(elementId).innerText;

        // Create a temporary textarea element to hold the JSON data
        var textarea = document.createElement('textarea');
        textarea.value = jsonData;
        document.body.appendChild(textarea);

        // Select the JSON data in the textarea
        textarea.select();
        textarea.setSelectionRange(0, 99999); // For mobile devices

        // Copy the selected JSON data to the clipboard
        document.execCommand('copy');

        // Remove the temporary textarea element
        document.body.removeChild(textarea);

        // Optionally, provide some feedback to the user
        var alertDiv = document.createElement('div');
            alertDiv.className = 'bg-green-500 text-white px-2 py-1 rounded-lg flex items-center';
            alertDiv.setAttribute('role', 'alert');
            alertDiv.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span>JSON has been copied!</span>
            `;
            document.getElementById('alertContainer').appendChild(alertDiv);

            // Remove the alert after 3 seconds
            setTimeout(function() {
                alertDiv.remove();
            }, 3000);
    }

    function toggleAndCopyData(elementId) {
        copyData(elementId); // Copy JSON data first
    }

    function showSpinner(elementId) {
        var spinners = document.querySelectorAll('#' + elementId + ' .spinner');
        spinners.forEach(function(spinner) {
            spinner.parentElement.classList.remove('hidden');
        });
    }

    function hideSpinner(elementId) {
        var spinners = document.querySelectorAll('#' + elementId + ' .spinner');
        spinners.forEach(function(spinner) {
            spinner.parentElement.classList.add('hidden');
        });
    }

    return {
        toggleItemData: toggleItemData,
        copyData: copyData,
        toggleAndCopyData: toggleAndCopyData,
        fetchData: fetchData
    };
})();