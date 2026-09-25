export async function GET() {
  try {
    const backendUrl = process.env.BACKEND_URL;

    if (!backendUrl) {
      return Response.json(
        { error: "BACKEND_URL is not configured" },
        { status: 500 }
      );
    }

    const response = await fetch(`${backendUrl}/api/deals`, {
      cache: "no-store",
    });

    if (!response.ok) {
      return Response.json(
        { error: `Backend returned ${response.status}` },
        { status: response.status }
      );
    }

    const data = await response.json();

    return Response.json(data);
  } catch (error) {
    console.error("Backend proxy error:", error);

    return Response.json(
      { error: "Unable to connect to FastAPI backend" },
      { status: 500 }
    );
  }
}
