onmessage = function(e) {
  // Receive the ImageBitmap and draw it on an OffscreenCanvas
  const imageBitmap = e.data.imageBitmap;

  // Assuming you need to create a new OffscreenCanvas in the worker
  const offscreenCanvas = new OffscreenCanvas(imageBitmap.width, imageBitmap.height);
  const ctx = offscreenCanvas.getContext('2d');

  // Now you can draw the ImageBitmap
  ctx.drawImage(imageBitmap, 0, 0);

  // Perform any additional drawing or processing as required
  // Note: Further operations or response back to the main thread can follow here
};
