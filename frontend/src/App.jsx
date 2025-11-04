import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleAnalyze = async () => {
    if (!file) return alert('Upload a file first!');
    const text = await file.text();
    setLoading(true);
    try {
      const res = await axios.post('http://127.0.0.1:5000/analyze', { content: text });
      setResult(res.data.results);
    } catch (err) {
      console.error(err);
      alert('Error analyzing file');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-indigo-200 via-pink-100 to-purple-200 text-gray-800">
      <h1 className="text-4xl font-bold mb-6 text-purple-700 drop-shadow-md">
        PrivacyLeak Hunter 🔍
      </h1>

      <div className="bg-white p-6 rounded-2xl shadow-xl w-96 text-center">
        <input type="file" onChange={handleFileChange} className="mb-4" />
        <button
          onClick={handleAnalyze}
          className="bg-purple-600 hover:bg-purple-700 text-white px-6 py-2 rounded-xl shadow-md transition-all"
        >
          {loading ? 'Analyzing...' : 'Analyze File'}
        </button>

        {result && (
          <div className="mt-6 text-left">
            <h2 className="font-semibold text-lg mb-2">Detected Sensitive Info:</h2>
            {Object.entries(result).map(([key, values]) => (
              <div key={key}>
                <strong>{key}:</strong> {values.length ? values.join(', ') : 'None found'}
              </div>
            ))}
          </div>
        )}
      </div>

      <footer className="mt-10 text-sm text-gray-500">
        © 2025 Kunal Badhan — Chandigarh University
      </footer>
    </div>
  );
};

export default App;
