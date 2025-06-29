from enum import Enum
from fastapi import APIRouter
from fastapi.responses import JSONResponse

TEXT = """# V7 Is Here! 🚀

> "The best file upload solution just got even better!" - _Tech Weekly_

This release has been an absurd amount of work. So proud of the team and what we've built. Huge thanks to [Julius](https://github.com/julius) and [Mark](https://github.com/mark) for making this happen.

---

It is so, so hard to not go straight into the nerdy details, but the whole point of UploadThing is that you don't need to know ANY of those details. With that in mind, here's what's relevant for most y'all:

- UploadThing is now _way_ faster
- Uploads can be **paused** and _resumed_ seamlessly
- ~~Old limitations removed~~
- More details...

## Performance Comparison

| Feature            | V6     | V7        |
| ------------------ | ------ | --------- |
| Upload Speed       | 10MB/s | 50MB/s    |
| Concurrent Uploads | 100    | Unlimited |
| Max File Size      | 2GB    | 10GB      |

## Revolutionary Features

We've completely overhauled our backend infrastructure to bring you unparalleled performance. Our new distributed processing system can handle millions of concurrent uploads without breaking a sweat.

### Code Example

```typescript
import { createUploadthing } from 'uploadthing/next';

const f = createUploadthing();

export const ourFileRouter = {
	imageUploader: f({ image: { maxFileSize: '4MB' } })
		.middleware(async () => {
			return { userId: 1234 };
		})
		.onUploadComplete(async ({ metadata, file }) => {
			console.log('Upload complete for userId:', metadata.userId);
		})
};
```

![Upload Dashboard](https://example.com/dashboard.png)

### AI-Powered Optimization

UploadThing now leverages cutting-edge machine learning algorithms to optimize your uploads in real-time.

<details>
<summary>Technical Details</summary>

- Uses TensorFlow.js for client-side optimizations
- Implements WebAssembly for performance
- Leverages Web Workers for background processing

</details>

## More Formatting Examples

### Advanced Markdown

#### Lists and Sublists

- Main Feature
  - Sub-feature 1
  - Sub-feature 2
    - Detailed point
    - Another detail
- Another Feature
  1. First step
  2. Second step
  3. Third step

#### Text Formatting

_Italic text_ and _another italic_
**Bold text** and **another bold**
**_Bold and italic_** **_together_**
~~Strikethrough text~~
`inline code`

### HTML Elements

<div align="center">
  <h3>Centered Content</h3>
  <p>This content is centered using `HTML`</p>
</div>

<kbd>Ctrl</kbd> + <kbd>C</kbd> to copy

<mark>Highlighted text</mark>

<blockquote>
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
</blockquote>

<details>
<summary>Click to expand</summary>
This is hidden content that can be expanded!

<ul>
  <li>Point 1</li>
  <li>Point 2</li>
  <li>Point 3</li>
</ul>
</details>

<aside>
💡 Pro tip: You can combine <code>HTML</code> and <code>Markdown</code> for powerful formatting
</aside>

### Custom Styling

<div style="background-color: #f0f0f0; padding: 1rem; border-radius: 4px;">
  <p style="color: #333;">Custom styled content box</p>
  <ul>
    <li>Feature highlight</li>
    <li>Important note</li>
  </ul>
</div>

---

_For more information, visit our [documentation](https://docs.uploadthing.com)._

```js
console.log('Hello, world!');
```

```js
console.log('Hello, world!');
console.log('Hello, world!');
console.log('Hello, world!');
```

[![Why React Hooks are the Future of React Development](https://medium.com/@johndoe/why-react-hooks-are-the-future)](https://miro.medium.com/v2/resize:fit:320/1*abc123.jpg)
> **Why React Hooks are the Future of React Development**
> Learn how React Hooks are revolutionizing the way we write components and manage state in React applications. Discover the benefits and best practices.
"""


class ServiceName(str, Enum):
    MEDIUM = "medium"
    TWITTER = "twitter"


async def render_page(service_name: ServiceName):
    return JSONResponse(
        content={
            "text": TEXT,
            "service_name": service_name.value,
            "article": {
                "title": "UploadThing is 5x Faster",
                "date": "2024-09-13T12:00:00Z",
                "author": {
                    "name": "Theo Browne",
                    "role": "CEO @ Ping Labs",
                    "avatar": "https://picsum.photos/seed/post1/400/300",
                },
                "postImage": "https://picsum.photos/seed/postimage/1200/600",
                "tableOfContents": [
                    {"id": "v7-is-here", "title": "V7 Is Here!"},
                    {"id": "benchmarks", "title": "Benchmarks"},
                    {"id": "the-road-to-v7", "title": "The Road To V7"},
                    {
                        "id": "uploadthing-has-served",
                        "title": "UploadThing Has Served...",
                    },
                    {
                        "id": "and-were-just-getting-started",
                        "title": "...and we're just getting started",
                    },
                ],
            },
        }
    )


def register_render_router(router: APIRouter) -> None:
    render_router = APIRouter(prefix="/services")

    async def render_service_page(service_name: ServiceName):
        return await render_page(service_name)

    for method in ["GET", "HEAD"]:
        render_router.add_api_route(
            "/{service_name}/render",
            endpoint=render_service_page,
            methods=[method],
            summary="Render service page",
            description="Render service page",
            operation_id=f"render_page_{method}",
            tags=["render"],
        )

    router.include_router(render_router)
