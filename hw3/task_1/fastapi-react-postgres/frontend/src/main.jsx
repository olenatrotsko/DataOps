
import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState('');
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);

  const loadItems = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch('/api/items');

      if (!response.ok) {
        throw new Error(`API returned ${response.status}`);
      }

      setItems(await response.json());
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const createItem = async (event) => {
    event.preventDefault();

    const itemName = name.trim();
    if (!itemName || saving) return;

    setSaving(true);
    setError(null);

    try {
      const response = await fetch('/api/items', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: itemName,
        }),
      });

      if (!response.ok) {
        throw new Error(`API returned ${response.status}`);
      }

      setName('');
      await loadItems();
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  };

  useEffect(() => {
    loadItems();
  }, []);

  return (
    <main className="card">
      <h1>FastAPI + React + PostgreSQL</h1>

      <p>Create and view items stored in PostgreSQL.</p>

      <form onSubmit={createItem}>
        <input
          type="text"
          placeholder="Enter item name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <button type="submit" disabled={saving || !name.trim()}>
          {saving ? 'Saving...' : 'Create Item'}
        </button>
      </form>

      <button onClick={loadItems} disabled={loading}>
        Refresh
      </button>

      {loading && <p>Loading...</p>}

      {error && <p className="error">Error: {error}</p>}

      {!loading && (
        <ul>
          {items.map((item) => (
            <li key={item.id}>
              {item.id}. {item.name}
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
