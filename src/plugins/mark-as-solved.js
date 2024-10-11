const topics = require.main.require('./src/topics');
const posts = require.main.require('./src/posts');
const privileges = require.main.require('./src/privileges');

module.exports = function(socket, callback) {
    socket.on('plugins.markAsSolved', async (data, callback) => {
        const { tid, pid } = data;

        try {
            // Fetch the topic and check if the user has permission to mark as solved
            const topic = await topics.getTopicData(tid);
            const canMarkAsSolved = await privileges.posts.canEdit(pid, socket.uid);

            if (!canMarkAsSolved) {
                return callback(new Error('You do not have permission to mark as solved.'));
            }

            // Mark the post as solved in the database
            await posts.setPostField(pid, 'solved', 1);

            // Optionally mark the entire topic as solved
            await topics.setTopicField(tid, 'solved', 1);

            // Success callback with more detailed response
            callback(null, { message: 'Post and topic marked as solved.', tid, pid });
        } catch (err) {
            // Handle any errors during the process
            callback(new Error('An error occurred while marking the post as solved.'));
        }
    });
};

function markAsSolved(tid, pid) {
    socket.emit('plugins.markAsSolved', { tid: tid, pid: pid }, function (err, data) {
        if (err) {
            app.alertError(err.message);
        } else {
            app.alertSuccess('Post marked as solved!');

            // Update UI: Hide the button and show the "Solved" label
            document.querySelector(`[data-pid="${pid}"] .mark-as-solved`).style.display = 'none';
            document.querySelector(`[data-pid="${pid}"] .solved-label`).style.display = 'block';
        }
    });
}
