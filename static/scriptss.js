document.addEventListener('DOMContentLoaded', () => {
    fetch('/hod_dashboard')
        .then(response => response.json())
        .then(request_id => {
            const pendingRequestsList = document.getElementBid('request_id');

            request_id.forEach(data => {
                const listItem = document.createElement('li');
                listItem.innerHTML = `
                    <strong>Employee ID:</strong> ${data.id}<br>
                    <strong>Request ID:</strong> ${data.request_id}<br>
                    <strong>Leave Type:</strong> ${data.leavetype}<br>
                    <strong>Start Date:</strong> ${data.start_date}<br>
                    <strong>End Date:</strong> ${data.end_date}<br>
                    <button onclick="approveRequest(${data.request_id})">Approve</button>
                    <button onclick="rejectRequest(${data.request_id})">Reject</button>
                `;
                pendingRequestsList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error fetching pending requests:', error);
        });
});

function approve(request_id) {
    fetch(`/approve/${request_id}`)
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            location.reload();
        })
        .catch(error => {
            console.error('Error approving request:', error);
        });
}

function reject(request_id) {
    fetch(`/reject/${request_id}`)
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            location.reload();
        })
        .catch(error => {
            console.error('Error rejecting request:', error);
        });
}