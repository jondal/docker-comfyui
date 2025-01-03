|name | description| 
| - | - |
| Animation Builder (mtb) | Convenient way to manage basic animation maths at the core of many of my workflows| 
| Any To String (mtb) | Tries to take any input and convert it to a string| 
| Bbox (mtb) | The bounding box (BBOX) custom type used by other nodes| 
| Bbox From Mask (mtb) | From a mask extract the bounding box| 
| Blur (mtb) | Blur an image using a Gaussian filter.| 
| Color Correct (mtb) | Various color correction methods| 
| Colored Image (mtb) | Constant color image of given size| 
| Concat Images (mtb) | Add images to batch| 
| Crop (mtb) | Crops an image and an optional mask to a given bounding box\n\n    The bounding box can be given as a tuple of (x, y, width, height) or as a BBOX type\n    The BBOX input takes precedence over the tuple input\n|| 
| Debug (mtb) | Experimental node to debug any Comfy values, support for more types and widgets is planned| 
| Deep Bump (mtb) | Normal & height maps generation from single pictures| 
| Export With Ffmpeg (mtb) | Export with FFmpeg (Experimental)| 
| Face Swap (mtb) | Face swap using deepinsight/insightface models| 
| Film Interpolation (mtb) | Google Research FILM frame interpolation for large motion| 
| Fit Number (mtb) | Fit the input float using a source and target range| 
| Float To Number (mtb) | Node addon for the WAS Suite. Converts a \"comfy\" FLOAT to a NUMBER.| 
| Get Batch From History (mtb) | Very experimental node to load images from the history of the server.\n\n    Queue items without output are ignored in the count.| 
| Image Compare (mtb) | Compare two images and return a difference image| 
| Image Distort With Uv (mtb) | Distorts an image based on a UV map.| 
| Image Premultiply (mtb) | Premultiply image with mask| 
| Image Remove Background Rembg (mtb) | Removes the background from the input using Rembg.| 
| Image Resize Factor (mtb) | Extracted mostly from WAS Node Suite, with a few edits (most notably multiple image support) and less features.| 
| Image To Uv (mtb) | Turn an image back into a UV map. (Shallow converter)| 
| Int To Bool (mtb) | Basic int to bool conversion| 
| Int To Number (mtb) | Node addon for the WAS Suite. Converts a \"comfy\" INT to a NUMBER.| 
| Latent Lerp (mtb) | Linear interpolation (blend) between two latent vectors| 
| Load Face Analysis Model (mtb) | Loads a face analysis model| 
| Load Face Enhance Model (mtb) | Loads a GFPGan or RestoreFormer model for face enhancement. (https://civitai.com/models/24690/comfyui-facerestore-node look like a better alternative)| 
| Load Face Swap Model (mtb) | Loads a faceswap model| 
| Load Film Model (mtb) | Loads a FILM model| 
| Load Image From Url (mtb) | Load an image from the given URL| 
| Load Image Sequence (mtb) | Load an image sequence from a folder. The current frame is used to determine which image to load.\n\n    Usually used in conjunction with the `Primitive` node set to increment to load a sequence of images from a folder.\n    Use -1 to load all matching frames as a batch.\n|| 
| Mask To Image (mtb) | Converts a mask (alpha) to an RGB image with a color and background| 
| Qr Code (mtb) | Basic QR Code generator| 
| Restore Face (mtb) | Uses GFPGan to restore faces| 
| Save Gif (mtb) | Save the images from the batch as a GIF| 
| Save Image Grid (mtb) | Save all the images in the input batch as a grid of images.| 
| Save Image Sequence (mtb) | Save an image sequence to a folder. The current frame is used to determine which image to save.\n\n    This is merely a wrapper around the `save_images` function with formatting for the output folder and filename.\n|| 
| Save Tensors (mtb) | Save torch tensors (image, mask or latent) to disk, useful to debug things outside comfy| 
| Smart Step (mtb) | Utils to control the steps start/stop of the KAdvancedSampler in percentage| 
| String Replace (mtb) | Basic string replacement| 
| Styles Loader (mtb) | Load csv files and populate a dropdown from the rows (\u00e0 la A111)| 
| Text To Image (mtb) | Utils to convert text to image using a font\n\n\n    The tool looks for any .ttf file in the Comfy folder hierarchy.\n|| 
| Transform Image (mtb) | Save torch tensors (image, mask or latent) to disk, useful to debug things outside comfy\n\n\n    it return a tensor representing the transformed images with the same shape as the input tensor\n|| 
| Uncrop (mtb) | Uncrops an image to a given bounding box\n\n    The bounding box can be given as a tuple of (x, y, width, height) or as a BBOX type\n    The BBOX input takes precedence over the tuple input| 
| Unsplash Image (mtb) | Unsplash Image given a keyword and a size| 
| Uv Distort (mtb) | Applies a polar coordinates or wave distortion to the UV map| 
| Uv Map (mtb) | Generates a UV Map tensor given a widht and height| 
| Uv Remove Seams (mtb) | Blends values near the UV borders to mitigate visible seams.| 
| Uv Tile (mtb) | Tiles the UV map based on the specified number of tiles.| 
| Uv To Image (mtb) | Converts the UV map to an image. (Shallow converter)| 


