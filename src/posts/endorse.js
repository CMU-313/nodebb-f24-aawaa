'use strict';

const plugins = require('../plugins');

module.exports = function (Posts) {
	Posts.endorse = async function (pid, uid) {
		return await toggleEndorse('endorse', pid, uid);
	};

	Posts.unendorse = async function (pid, uid) {
		return await toggleEndorse('unendorse', pid, uid);
	};

	async function toggleEndorse(type, pid, uid) {
		const isEndorsing = type === 'endorse';
		await plugins.hooks.fire(`filter:post.${type}`, { pid: pid, uid: uid });

		await Posts.setPostFields(pid, {
			endorse: isEndorsing ? 1 : 0,
			endorseUid: isEndorsing ? uid : 0,
		});

		const postData = await Posts.getPostFields(pid, ['pid', 'tid', 'uid', 'content', 'timestamp']);

		return postData;
	}
};
