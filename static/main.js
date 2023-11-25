document.addEventListener('DOMContentLoaded', function() {
    // fetch and update the library
    function updateLibrary(selectedFilter) {
        fetch('/get_library', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + selectedFilter,
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('library-section').innerHTML = data.library_html;
        });
    }

    // Get the initial library on page load
    updateLibrary(document.getElementById('type').value);

    // "Get Random Friend-a-mendation" button
    document.getElementById('random-btn').addEventListener('click', function() {
        var selectedFilter = document.getElementById('type').value;
        fetch('/get_recommendation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + selectedFilter,
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById('library-section').innerHTML = '<div class="friend-a-mendation flipped">' + data + '</div>';
        });
    });

    // library type dropdown
    document.getElementById('type').addEventListener('change', function() {
        var selectedFilter = this.value;
        updateLibrary(selectedFilter);
    });



    // Event listener for clicking on friend-a-mendation to flip the card
    // document.addEventListener('click', function(event) {
    //     var clickedElement = event.target;
    //     if (clickedElement.classList.contains('friend-a-mendation')) {
    //         toggleCard(clickedElement);
    //     }
    // });
});

function fetchLibrary() {
    fetch('/get_library', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'type=all',  // Fetch all categories
    })
    .then(response => response.json())
    .then(data => {
        var librarySection = document.getElementById('library-section');
        librarySection.innerHTML = data.library_html;
    });
}


// function toggleCard(element) {
//     element.classList.toggle('flipped');
//     // Toggle the visibility of the back side
//     var backElement = element.querySelector('.back');
//     backElement.style.display = backElement.style.display === 'none' ? 'block' : 'none';
// }


document.addEventListener('DOMContentLoaded', function() {
    // fetch and update the library
    function updateLibrary(selectedFilter) {
        fetch('/get_library', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + selectedFilter,
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('library-section').innerHTML = data.library_html;
        });
    }

    // Get the initial library on page load (fetch all categories)
    updateLibrary('all');

    // Event listener for the "Get Random Friend-a-mendation" button
    document.getElementById('random-btn').addEventListener('click', function() {
        var selectedFilter = document.getElementById('type').value;
        fetch('/get_recommendation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + selectedFilter,
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById('library-section').innerHTML = '<div class="friend-a-mendation flipped">' + data + '</div>';
        });
    });

    // Event listener for the library type dropdown
    // Uncomment the following lines if you plan to use a dropdown again
    // document.getElementById('type').addEventListener('change', function() {
    //     var selectedFilter = this.value;
    //     updateLibrary(selectedFilter);
    // });

    // ... (rest of your script)


    
    
});


document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch and update the library
    function updateLibrary(selectedFilter) {
        fetch('/get_library', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + selectedFilter,
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('library-section').innerHTML = data.library_html;
            scrollLibrary(0); // Reset scroll position
        });
    }

    // Get the initial library on page load
    updateLibrary('all');

    // Event listener for the "Get Random Friend-a-mendation" button
    document.getElementById('random-btn').addEventListener('click', function() {
        var selectedFilter = document.getElementById('type').value;
        fetch('/get_recommendation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + selectedFilter,
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById('library-section').innerHTML = '<div class="friend-a-mendation flipped">' + data + '</div>';
        });
    });

    // library type dropdown
    document.getElementById('type').addEventListener('change', function() {
        var selectedFilter = this.value;
        updateLibrary(selectedFilter);
    });

 

    // handle scrolling
    function scrollLibrary(direction) {
        var librarySection = document.getElementById('library-section');
        librarySection.scrollLeft += direction * librarySection.clientWidth;
    }
});

