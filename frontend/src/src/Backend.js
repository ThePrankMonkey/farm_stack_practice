import { useState } from "react";

function Backend() {
  const [data, setData] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [err, setErr] = useState("");

  const handleClick = async () => {
    setIsLoading(true);

    try {
      const response = await fetch("http://localhost:8000/r/", {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      });

      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      const result = await response.json();

      console.log("result is: ", JSON.stringify(result, null));

      setData(result);
    } catch (err) {
      setErr(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      {err && <h2>{err}</h2>}
      <button onClick={handleClick}>Fetch data</button>
      {isLoading && <h2>Loading...</h2>}
      {data &&
        Object.entries(data).map(([key, value]) => (
          <div key={key}>
            My key is {key} and my value is {value}
          </div>
        ))}
    </div>
  );
}

export default Backend;
