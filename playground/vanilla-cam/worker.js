onmessage = function(e) {
  const offscreenCanvas = e.data.canvas;
  const ctx = offscreenCanvas.getContext('2d');

  // Perform drawing operations
  ctx.fillStyle = 'red';
  ctx.fillRect(10, 10, 50, 50);

  // Note: You can't directly add the OffscreenCanvas to the DOM
  // but you can postMessage data back to the main thread or manipulate
  // image data for further processing (like in computer vision tasks)
};
