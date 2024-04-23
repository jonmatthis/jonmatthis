self.addEventListener('message', async (event) => {
  const { deviceId } = event.data;

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: { deviceId } });
    const videoTrack = stream.getVideoTracks()[0];

    // Check if getCapabilities is available
    if (videoTrack.getCapabilities) {
      const capabilities = videoTrack.getCapabilities();
      const settings = videoTrack.getSettings();

      if (capabilities && settings) {
        const maxResolution = {
          width: capabilities.width.max,
          height: capabilities.height.max
        };

        // Apply the maximum resolution
        await videoTrack.applyConstraints({
          advanced: [{ width: maxResolution.width, height: maxResolution.height }]
        });

        const newSettings = videoTrack.getSettings();
        self.postMessage({ deviceId, maxResolution, settings: newSettings });
      }
    } else {
      console.log('getCapabilities not supported by this browser.');
    }
  } catch (e) {
    console.error('Error accessing camera feed:', e);
  }
});
