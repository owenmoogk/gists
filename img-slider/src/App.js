import ReactCompareImage from 'react-compare-image';

function App() {
  return (
    <div className="App" style={{height: '100000px', width: '500px'}}>
      <ReactCompareImage leftImage='test1.png' rightImage='test2.png' aspectRatio='taller' handle={
        <button style={{
          height: '50px',
          outline: 'none',
          width: '10px',
          border: 'none',
          borderRadius: '5px',
        }}></button>
      }/>
    </div>
  );
}

export default App;
