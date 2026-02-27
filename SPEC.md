# Air Quality Index App Specification

## Project Overview
- **Project Name**: AirWise - Air Quality Index Dashboard
- **Type**: Single-page web application
- **Core Functionality**: Display current, forecast, and historical air quality data for any searched location
- **Target Users**: General public, health-conscious individuals, travelers

## API Information
- **Base URL**: `http://api.openweathermap.org/data/2.5`
- **API Key**: `fd9da1f66789a327c94c926a129bd73c`
- **Endpoints Used**:
  - Current Air Pollution: `/air_pollution?lat={lat}&lon={lon}`
  - Forecast Air Pollution (5-day/3-hour): `/air_pollution/forecast?lat={lat}&lon={lon}`
  - Geocoding: `/geo/1.0/direct?q={city}&limit=1`

## UI/UX Specification

### Layout Structure
- **Header**: Fixed top navigation with app logo and title
- **Search Section**: Centered search bar with location autocomplete
- **Main Content**: Three-column grid showing Current, Forecast, and Historical data
- **Footer**: Minimal footer with credits

### Responsive Breakpoints
- **Desktop**: 1200px+ (3 columns)
- **Tablet**: 768px-1199px (2 columns)
- **Mobile**: <768px (1 column, stacked)

### Visual Design

#### Color Palette
- **Background**: `#0a0e17` (deep night blue)
- **Card Background**: `#131a2b` (dark navy)
- **Card Border**: `#1e2a42` (subtle blue border)
- **Primary Accent**: `#00d4aa` (vibrant teal)
- **Secondary Accent**: `#7c3aed` (electric purple)
- **Warning**: `#f59e0b` (amber)
- **Danger**: `#ef4444` (red)
- **Good Air Quality**: `#10b981` (emerald green)
- **Text Primary**: `#f1f5f9` (off-white)
- **Text Secondary**: `#94a3b8` (muted gray)

#### AQI Color Scale
- Good (1): `#10b981` (green)
- Fair (2): `#84cc16` (lime)
- Moderate (3): `#f59e0b` (amber)
- Poor (4): `#f97316` (orange)
- Very Poor (5): `#ef4444` (red)
- Extremely Poor (6): `#7f1d1d` (dark red)

#### Typography
- **Font Family**: "Outfit" (Google Fonts) - modern geometric sans-serif
- **Headings**: 700 weight
  - H1: 2.5rem
  - H2: 1.75rem
  - H3: 1.25rem
- **Body**: 400 weight, 1rem
- **Small**: 0.875rem

#### Spacing System
- **Base unit**: 8px
- **Section padding**: 48px (6 units)
- **Card padding**: 24px (3 units)
- **Element gap**: 16px (2 units)

#### Visual Effects
- **Card shadows**: `0 8px 32px rgba(0, 212, 170, 0.08)`
- **Glassmorphism**: `backdrop-filter: blur(12px)` on cards
- **Gradient accents**: Linear gradient from teal to purple on key elements
- **Animations**: 
  - Fade-in on data load (0.5s ease)
  - Scale hover on cards (1.02 transform)
  - Pulse animation on AQI indicator

### Components

#### Search Bar
- Rounded pill shape with gradient border
- Search icon on left
- Clear button on right when text present
- Loading spinner during search

#### AQI Gauge (Current Data)
- Large circular gauge with gradient fill
- Central numeric display (1-6 scale)
- AQI category text below
- Animated on load

#### Pollutant Breakdown Cards
- CO, NO₂, O₃, PM2.5, PM10, SO₂ display
- Horizontal bar charts with percentage fill
- Color-coded by severity

#### Forecast Section
- 5-day forecast cards
- Each card shows: day name, AQI value, AQI category
- Color-coded backgrounds matching AQI level

#### Historical Section
- Last 7 days data
- Line chart visualization showing trends
- Min/Max/Average indicators

## Functionality Specification

### Core Features
1. **Location Search**
   - Text input with city name
   - Geocoding to get lat/lon coordinates
   - Error handling for invalid locations

2. **Current AQI Display**
   - Real-time air quality index (1-6 scale)
   - Individual pollutant concentrations
   - Health recommendations based on AQI

3. **Forecast Data**
   - 5-day air quality forecast
   - 3-hour interval data aggregated to daily
   - Best and worst days highlighted

4. **Historical Data**
   - Previous 7 days of AQI data
   - Trend visualization
   - Comparison to current day

### User Interactions
- Search submission on Enter key or button click
- Loading states during API calls
- Error messages for failed requests
- Empty state when no search performed

### Data Handling
- Parse API responses into readable format
- Convert pollutant concentrations to μg/m³
- Calculate AQI category from component values
- Store last searched location in localStorage

### Edge Cases
- Handle cities not found
- Handle API rate limits
- Handle network errors gracefully
- Handle empty forecast/historical data

## Acceptance Criteria
1. ✓ Search returns valid location and displays data
2. ✓ Current AQI shows accurate index value (1-6)
3. ✓ All 6 pollutants displayed with values
4. ✓ Forecast shows 5 days of data
5. ✓ Historical shows trend visualization
6. ✓ Responsive on all device sizes
7. ✓ Smooth animations and transitions
8. ✓ Error handling for invalid searches
9. ✓ Loading states visible during API calls
10. ✓ Design matches specified color palette and typography
